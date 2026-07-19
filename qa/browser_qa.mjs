#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import process from "node:process";
import { pathToFileURL } from "node:url";
import { chromium } from "playwright";

const args = process.argv.slice(2);
const configPath = args[0] || "config/targets.json";
const outDir = args[1] || "reports/browser-qa";
fs.mkdirSync(outDir, { recursive: true });

const config = JSON.parse(fs.readFileSync(configPath, "utf8"));
const viewports = [
  { name: "desktop", width: 1440, height: 1000 },
  { name: "tablet", width: 1024, height: 768 },
  { name: "mobile", width: 390, height: 844 }
];

const browser = await chromium.launch({ headless: true });
const results = [];

for (const target of config.targets) {
  const targetResult = {
    id: target.id,
    source: target.source,
    started_at: new Date().toISOString(),
    viewports: [],
    final_decision: "PASS",
    errors: []
  };

  for (const vp of viewports) {
    const context = await browser.newContext({
      viewport: { width: vp.width, height: vp.height },
      acceptDownloads: true,
      ignoreHTTPSErrors: false
    });
    const page = await context.newPage();

    const consoleErrors = [];
    const pageErrors = [];
    const failedRequests = [];
    const downloads = [];

    page.on("console", msg => {
      if (msg.type() === "error") consoleErrors.push(msg.text());
    });
    page.on("pageerror", err => pageErrors.push(String(err)));
    page.on("requestfailed", req => {
      failedRequests.push({
        url: req.url(),
        method: req.method(),
        failure: req.failure()?.errorText || "unknown"
      });
    });
    page.on("download", async d => {
      downloads.push({
        suggestedFilename: d.suggestedFilename(),
        url: d.url()
      });
      await d.cancel().catch(() => {});
    });

    let navigationStatus = "PASS";
    let navigationError = null;
    const url = pathToFileURL(path.resolve(target.source)).href;

    try {
      await page.goto(url, { waitUntil: "domcontentloaded", timeout: 45000 });
      await page.waitForTimeout(4000);
    } catch (err) {
      navigationStatus = "BLOCKED";
      navigationError = String(err);
    }

    const metrics = navigationStatus === "PASS" ? await page.evaluate(() => ({
      title: document.title,
      bodyTextLength: document.body?.innerText?.length || 0,
      scrollWidth: document.documentElement.scrollWidth,
      clientWidth: document.documentElement.clientWidth,
      scrollHeight: document.documentElement.scrollHeight,
      clientHeight: document.documentElement.clientHeight,
      horizontalOverflow: document.documentElement.scrollWidth > document.documentElement.clientWidth + 2,
      canvasCount: document.querySelectorAll("canvas").length,
      svgCount: document.querySelectorAll("svg").length,
      buttonCount: document.querySelectorAll("button").length,
      linkCount: document.querySelectorAll("a").length,
      hiddenOverflow: getComputedStyle(document.documentElement).overflow === "hidden"
    })) : {};

    const interactionResults = [];
    if (navigationStatus === "PASS") {
      for (const selector of target.interaction_selectors || []) {
        try {
          const locator = page.locator(selector).first();
          if (await locator.count()) {
            await locator.click({ timeout: 3000 });
            await page.waitForTimeout(400);
            interactionResults.push({ selector, status: "PASS" });
          } else {
            interactionResults.push({ selector, status: "WARN", note: "not found" });
          }
        } catch (err) {
          interactionResults.push({ selector, status: "WARN", note: String(err) });
        }
      }
    }

    const shot = path.join(outDir, `${target.id}-${vp.name}.png`);
    if (navigationStatus === "PASS") {
      await page.screenshot({ path: shot, fullPage: false }).catch(() => {});
    }

    let decision = "PASS";
    if (navigationStatus === "BLOCKED" || pageErrors.length > 0) decision = "BLOCKED";
    else if (consoleErrors.length > 0 || failedRequests.length > 0 || metrics.horizontalOverflow) decision = "WARN";

    targetResult.viewports.push({
      viewport: vp,
      navigationStatus,
      navigationError,
      metrics,
      consoleErrors,
      pageErrors,
      failedRequests,
      downloads,
      interactions: interactionResults,
      screenshot: shot,
      decision
    });

    await context.close();
  }

  const decisions = targetResult.viewports.map(x => x.decision);
  if (decisions.includes("BLOCKED")) targetResult.final_decision = "BLOCKED";
  else if (decisions.includes("WARN")) targetResult.final_decision = "WARN";

  results.push(targetResult);
}

await browser.close();

const report = {
  harness_version: "2.0.0",
  generated_at: new Date().toISOString(),
  results
};
fs.writeFileSync(path.join(outDir, "browser-qa-report.json"), JSON.stringify(report, null, 2) + "\n");
console.log(path.resolve(outDir, "browser-qa-report.json"));
