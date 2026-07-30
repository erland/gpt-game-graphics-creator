# Knowledge Manifest

## Purpose

Define the planned knowledge architecture for Game Graphics Creator, with clear ownership and minimal overlap. The target is no more than 20 knowledge files.

## Planned knowledge files

1. `01-ROLE-AND-RESPONSIBILITY.md`
2. `02-ASSET-REQUEST-AND-DELIVERY-CONTRACT.md`
3. `03-ART-DIRECTION-AND-STYLE-LOCK.md`
4. `04-ASSET-MATURITY-AND-VALIDATION.md`
5. `05-TILESETS-AND-TILEMAP-ASSETS.md`
6. `06-SPRITES-AND-CHARACTER-SETS.md`
7. `07-ANIMATION-SHEETS.md`
8. `08-ISOMETRIC-ASSETS.md`
9. `09-UI-ICONS-AND-SIGNAGE.md`
10. `10-VFX-BACKGROUNDS-AND-PARALLAX.md`
11. `11-PROGRAMMATIC-POST-PROCESSING.md`
12. `12-ZIP-WORKFLOW-AND-RELEASE.md`
13. `13-ORIGINALITY-REFERENCES-AND-RIGHTS.md`
14. `14-PIXEL-ART-PIPELINE.md`
15. `15-HIGH-RESOLUTION-2D-PIPELINE.md`

## Architecture rules

- The main instruction contains only global behavior and non-negotiable boundaries.
- Each knowledge file owns one primary domain.
- Shared rules are defined once in the file that owns them and referenced elsewhere.
- Schemas and normative field definitions belong to the contract or validation owner, not duplicated in pipeline files.
- Asset-specific files may add stricter rules but must not redefine global maturity statuses or validation status meanings.
- Examples must not silently become normative rules.
- Builder-facing metadata belongs in `builder/`, not knowledge files.
- Test cases and fixtures belong outside the permanent knowledge set unless later evaluation shows that a compact test-reference file improves behavior.

## Implementation status at 1.0.0-rc2

Implemented:
- `01-ROLE-AND-RESPONSIBILITY.md`
- `02-ASSET-REQUEST-AND-DELIVERY-CONTRACT.md`
- `03-ART-DIRECTION-AND-STYLE-LOCK.md`
- `04-ASSET-MATURITY-AND-VALIDATION.md`
- `05-TILESETS-AND-TILEMAP-ASSETS.md`
- `06-SPRITES-AND-CHARACTER-SETS.md`
- `07-ANIMATION-SHEETS.md`
- `08-ISOMETRIC-ASSETS.md`
- `09-UI-ICONS-AND-SIGNAGE.md`
- `10-VFX-BACKGROUNDS-AND-PARALLAX.md`
- `11-PROGRAMMATIC-POST-PROCESSING.md`
- `12-ZIP-WORKFLOW-AND-RELEASE.md`
- `13-PROTOTYPE-TO-PRODUCTION-ART.md`

Reserved for future expansion, not required for this release candidate:
- `14-ORIGINALITY-REFERENCES-AND-RIGHTS.md`
- `15-PIXEL-ART-PIPELINE.md`
- `16-HIGH-RESOLUTION-2D-PIPELINE.md`