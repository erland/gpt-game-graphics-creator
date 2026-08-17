# Game Graphics Creator GPT

Game Graphics Creator is a Custom GPT package for creating, structuring, validating and revising technically usable graphics for 2D and isometric games. The repository contains the current Builder configuration, permanent Knowledge, reusable contracts/fixtures, regression tests and distribution tooling.

## Current status

- Version: `1.0.0-rc2`
- Permanent Knowledge: 13 files, defined by `builder/UPLOAD-MANIFEST.md`
- GPT Preview regression pack: G01–G16
- Publication: keep private until the required manual Preview tests have been executed and accepted

The repository no longer stores prompt-by-prompt implementation reports or old preflight snapshots; Git history is the source for that development history.

## Structure

- `builder/` — current GPT Builder fields, capability guidance and upload manifest
- `knowledge/` — normative GPT Knowledge files
- `contract/` — schemas and reusable request/delivery templates
- `fixtures/` — reusable positive and negative Preview fixtures
- `tests/` — G01–G16 regression cases and test manifest
- `docs/` — active maintainer guidance and release checklist
- `portable/` — entry point for the portable Chat package
- `scripts/` — distribution build and validation
- `.github/workflows/` — CI/release packaging

## Builder setup

1. Copy `builder/NAME.txt`, `builder/DESCRIPTION.md` and `builder/MAIN-INSTRUCTION.md` into the matching Builder fields.
2. Add the prompts from `builder/CONVERSATION-STARTERS.md`.
3. Configure capabilities according to `builder/CAPABILITIES.md`.
4. Upload exactly the permanent Knowledge files marked in `builder/UPLOAD-MANIFEST.md`.
5. Keep the GPT private while validating it.
6. Run G01–G16 from `tests/` and record actual result/evidence.
7. Resolve blocking failures before expanding visibility.

## Regression and release checks

Before a release:

- run G01–G16 in GPT Preview;
- verify the main instruction remains within the Builder size limit;
- verify the Knowledge upload count and manifest;
- parse/validate relevant YAML schemas and contract templates;
- verify no generated cache, nested release archive or OS metadata is included;
- build and validate both distribution ZIPs.

`docs/RELEASE-CHECKLIST.md` contains the maintainer checklist.

## Portable Chat and distribution builds

The repository builds two synchronized distributions from the current Builder configuration:

- `game-graphics-creator-custom-gpt-vX.Y.Z.zip` — Builder configuration, 13 approved permanent Knowledge files, and contract schemas/templates.
- `game-graphics-creator-chat-vX.Y.Z.zip` — portable package for a normal ChatGPT conversation, starting at `START-HERE.md`.

Local build:

```bash
python3 scripts/build_distributions.py
python3 scripts/validate_distributions.py
```

Push, pull-request and manual runs use `VERSION`. A published GitHub Release uses its `v<semver>` tag as the package version and attaches both ZIP files to the release.
