# Game Graphics Creator GPT — Release Candidate

This package contains the cumulative result of Prompts A–H from the implementation plan:

- GPT identity, scope and responsibility boundaries
- Main instruction below the Builder limit
- Knowledge architecture and anti-overlap rules
- Asset Request and Delivery Contract
- Machine-readable schemas and reusable templates
- Art direction and style locking
- Separate pipelines for tiles, isometry, sprites, animation, UI, icons, VFX, backgrounds and parallax
- Asset maturity, graphics-side validation and acceptance logic
- Deterministic post-processing, sheet assembly and manifest generation
- Revision triage and selective regeneration
- Safe zip intake, cleanup, versioning and cumulative release packaging
- Complete Builder configuration, capability guidance and upload manifest
- Reference fixtures and GPT Preview tests G01–G15
- Automated structural preflight and release-candidate documentation

## Package status

- Stage: Prompt H — Preflight and release candidate
- Version: `1.0.0-rc1`
- Publication status: Keep private until the required manual GPT Preview tests have been run and accepted
- Automated structural preflight: Passed
- Manual GPT Preview validation: Not yet run

`Release candidate` means the package is structurally ready for Builder setup and manual evaluation. It does not mean that the GPT, generated graphics, SpriteKit integration or physical-device behavior has been production verified.

## Structure

- `builder/` — GPT Builder fields, configuration, capabilities and upload manifest
- `knowledge/` — normative GPT knowledge files
- `contract/` — schemas and request/delivery templates
- `fixtures/` — reusable positive and negative Preview fixtures
- `tests/` — G01–G15 Preview test cases and test manifest
- `preflight/` — automated checks, manual-test matrix and release-candidate decision
- `docs/` — implementation history, ownership, release checklist and changelog

## Builder setup

1. Copy `builder/NAME.txt`, `DESCRIPTION.md` and `MAIN-INSTRUCTION.md` into the matching Builder fields.
2. Add the prompts from `builder/CONVERSATION-STARTERS.md`.
3. Configure capabilities according to `builder/CAPABILITIES.md`.
4. Upload exactly the permanent knowledge files marked in `builder/UPLOAD-MANIFEST.md`.
5. Keep the GPT private.
6. Run G01–G15 according to `preflight/MANUAL-PREVIEW-TESTS.md`.
7. Record evidence and resolve all blocking failures before expanding visibility.

## Verified in automated preflight

- Main instruction remains below 8,000 characters.
- Permanent knowledge upload count remains below 20 files.
- Required Builder and package files are present.
- YAML files and schemas parse successfully.
- Contract templates and fixtures validate against their schemas where applicable.
- G01–G15 and their expected/failure sections are present.
- Version and stage metadata are synchronized for this release candidate.
- No nested release archives, cache files or common OS metadata are included.
- Final archive integrity and clean extraction are verified during packaging.

## Still requires manual verification

- Actual GPT Builder upload and capability availability
- GPT Preview behavior for G01–G15
- Image-generation quality and identity consistency
- Real file creation and deterministic image inspection through the configured tools
- SpriteKit loading, gameplay collision, TV readability and physical Apple TV behavior

See `preflight/PREFLIGHT-REPORT.md` for the detailed decision.
