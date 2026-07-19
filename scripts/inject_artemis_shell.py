#!/usr/bin/env python3
from pathlib import Path
import argparse,re
NAV='<nav id="artemis-global-nav" style="position:fixed;top:0;left:0;right:0;z-index:99999;background:#0a0a0d;padding:10px 18px;font:600 13px system-ui;color:#eee"><a href="https://artemis.agoraxai.com" style="color:#d8ad67;text-decoration:none">ARTEMIS</a><span style="float:right"><a href="https://artemis.agoraxai.com" style="color:#eee;text-decoration:none;margin-right:18px">Back to Artemis</a><a href="https://agoraxai.com" style="color:#eee;text-decoration:none">AGOraXAI</a></span></nav><div style="height:44px"></div>'
FOOT='<footer id="artemis-global-footer" style="margin-top:32px;padding:24px 18px;background:#09090b;color:#bbb;font:500 12px system-ui">ARTEMIS · An AGOraXAI system · Preview output may require specialist review before production use.</footer>'
ap=argparse.ArgumentParser(); ap.add_argument("source"); ap.add_argument("--out",required=True); args=ap.parse_args()
text=Path(args.source).read_text(errors="replace")
if 'id="artemis-global-nav"' not in text: text=re.sub(r'(<body[^>]*>)',r'\1'+NAV,text,count=1,flags=re.I)
if 'id="artemis-global-footer"' not in text: text=re.sub(r'(</body>)',FOOT+r'\1',text,count=1,flags=re.I)
Path(args.out).parent.mkdir(parents=True,exist_ok=True); Path(args.out).write_text(text); print(Path(args.out).resolve())
