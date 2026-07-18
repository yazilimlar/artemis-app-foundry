# ARTEMIS App Foundry — Phase 1 Portfolio Intake Report

Generated: `2026-07-18T23:41:25+00:00`

## Executive findings

- The current portfolio spans geometry/fabrication, cultural intelligence, construction intelligence, and infrastructure intelligence.
- The two ZIP packages are compact release packages containing one HTML app plus briefs, test reports, and communications collateral.
- DEP Sewer applications should remain controlled or sanitization-gated until project, claims, actuals, GIS, and location data are reviewed.
- Diana applications require explicit preservation of embedded model licensing and attribution.
- The legacy geometry workbench should be archived within the geometric-workbench lineage rather than deployed as a separate product.

## Intake summary

| Source | Family | Recommended repository | Exposure | Risk | Notes |
|---|---|---|---|---|---|
| `ARTEMIS_v3_6_1_download(3).html` | geometry-fabrication | `artemis-geometric-workbench` | public-preview-candidate | low | 5 embedded data asset(s); 3 external domain(s); license/attribution review |
| `artemis_diana_threejs_viewer_STANDALONE_EMBEDDED(1).html` | cultural-intelligence | `artemis-diana` | public-preview-candidate | low | 1 embedded data asset(s); 1 external domain(s); license/attribution review |
| `artemis_diana_moonshot_demonstrator_v3(5).html` | cultural-intelligence | `artemis-diana` | public-preview-candidate | low | 1 embedded data asset(s); 1 external domain(s); license/attribution review |
| `Artemis_DEP_Sewer_Utility_Intelligence_Bridge_RC8_4_Dual_Story_Cockpit_Field_Claims_Hardened(4).html` | infrastructure-intelligence | `artemis-utility-intelligence` | internal | high | 7 external domain(s); license/attribution review |
| `Artemis_DEP_Sewer_Utility_Intelligence_Bridge_RC8_Public_Demo_GIS_Actuals_Clean(1).html` | infrastructure-intelligence | `artemis-utility-intelligence` | internal | high | 7 external domain(s); license/attribution review |
| `Artemis_Dynamic_Intelligence_Bridges_Phase_2_RC4_Package(1).zip` | construction-intelligence | `artemis-construction-intelligence` | internal | high | 6 files; HTML + briefs/test collateral |
| `Artemis_Dynamic_Intelligence_Bridges_Phase_3_RC5_DEP_Sewer_Package(1).zip` | infrastructure-intelligence | `artemis-utility-intelligence` | internal | high | 8 files; HTML + briefs/test collateral |

## ZIP package inventories

### Artemis_Dynamic_Intelligence_Bridges_Phase_2_RC4_Package(1).zip

- Members: 6
- Uncompressed size: 260,526 bytes
- Extensions: `{".html": 1, ".md": 4, ".pdf": 1}`

Included files:
- `Artemis_Construction_Intelligence_Bridge_RC4_Executive_Control_Room.html` — 243,897 bytes
- `Artemis_RC4_Phase_2_Executive_Control_Room_Brief.md` — 2,809 bytes
- `Artemis_RC4_LinkedIn_Post_Draft.md` — 1,934 bytes
- `Artemis_RC4_Screenshot_and_Video_Guide.md` — 1,821 bytes
- `Artemis_RC4_Test_Report.md` — 1,308 bytes
- `Artemis_RC4_Executive_Control_Room_Phase_2_Brief.pdf` — 8,757 bytes

### Artemis_Dynamic_Intelligence_Bridges_Phase_3_RC5_DEP_Sewer_Package(1).zip

- Members: 8
- Uncompressed size: 267,894 bytes
- Extensions: `{".html": 1, ".md": 6, ".pdf": 1}`

Included files:
- `Artemis_DEP_Sewer_Utility_Intelligence_Bridge_RC5.html` — 254,054 bytes
- `Artemis_RC5_Phase_3_DEP_Sewer_Standards_Brief.pdf` — 4,052 bytes
- `Artemis_RC5_Phase_3_DEP_Sewer_Standards_Brief.md` — 2,175 bytes
- `Artemis_RC5_LinkedIn_DEP_Sewer_Post.md` — 2,041 bytes
- `Artemis_RC5_Screenshot_and_Video_Guide.md` — 1,762 bytes
- `Artemis_RC5_Analytical_Feature_Highlights.md` — 1,447 bytes
- `Artemis_RC5_Test_Report.md` — 1,051 bytes
- `Artemis_RC6_Screenshot_Deck_and_Video_Mode_Prompt.md` — 1,312 bytes

## Release gates

### Public-preview gate
- Browser execution and console test
- Mobile and desktop acceptance test
- External dependency availability test
- Navigation back to Artemis and AGOraXAI
- Privacy, terms, analytics, and contact attribution

### Controlled-demo gate
- Data-owner approval
- Sanitization report
- Access-control decision
- Download/export review
- Screenshots checked for confidential information

### Commercial gate
- License and attribution review
- Security review
- Versioned project schema
- Support and incident ownership
- Product claims aligned with verified capability
