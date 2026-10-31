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

## GPT Byggaren 1.6.33 — current build contract

The authoritative behavior is `assistant/instructions.md`; the original Builder materials and 13 Knowledge files remain unchanged. The source project version is `1.0.0-rc2`.

**Built and package-validated:** ChatGPT Chat, Claude Projects, Claude Skills, OpenCode and OpenAI Plugin, plus project ZIP. **Not functionally host-verified:** image generation/editing, exact file processing, state, and delivery. Custom GPT remains historical, not a sixth active target. A package build does not establish host compatibility.

Build using the installed, original engine 1.6.33 scripts (no replacement packager):

```bash
python3 scripts/build_distributions.py --project-root . --version "$(cat VERSION)"
python3 scripts/validate_distributions.py --project-root .
```

The pinned original engine is installed in project `scripts/` and `templates/`; the detached engine ZIP is not needed in CI. `gpt-project.yaml` controls enabled runtime targets. See `docs/STEP-4-DISTRIBUTION-VERIFICATION.md` for measured checks and `docs/STEP-5-HYGIENE-REPORT.md` for CI/legacy inventory.

## Release and functional verification

G01–G16 remain unrun. Keep the project private and do not publish or activate other runtimes until relevant host-side graphics and asset-delivery tests have passed. CI checks source/package integrity only; it does not certify runtime behavior. A manual release decision and explicit functional evidence are required before attaching assets to any public release.

## Historical migration

Older GPT Byggaren 1.5 files are retained for provenance, not the active build authority. Their historic conclusions must not be interpreted as 1.6.33 release approval.
