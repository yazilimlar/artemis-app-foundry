# QA Acceptance Standard

## PASS
- Page loads
- No page exceptions
- No release-critical console errors
- No failed critical assets
- No horizontal overflow on mobile
- Required controls are present
- No blocked sanitization findings

## WARN
- Noncritical CDN failure
- Missing optional control
- Console warning/error without functional failure
- PII, GIS, claims, actuals, or license content requiring review
- Public-demo data not yet certified as synthetic/sanitized

## BLOCKED
- Embedded secrets
- Page exception or navigation failure
- Core WebGL/rendering failure
- Confidential or restricted data
- Public release conflicts with policy gate
