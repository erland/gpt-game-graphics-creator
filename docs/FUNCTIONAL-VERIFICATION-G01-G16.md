# G01–G16: evidence-based functional verification (2026-10-31)

## Method and decision

This check uses only inspected project files and deterministic Python checks. It **does not** execute a configured ChatGPT Chat host, call image generation, or open images in a game engine. The machine-readable evidence is `docs/evidence/G01-G16-static-evidence.json`. The checker is `tests/verify_static_contracts.py` and is runnable with `python tests/verify_static_contracts.py`.

The static check searches three canonical behavior source files for terms related to each G test; this is a **weak structural coverage heuristic, not a semantic or functional test**. Of 16 test definitions, 14 have all configured term probes in the source, while G02 and G13 merit manual inspection; absent terms do not show absent behavior. G02's precise 128x64 criterion is explicitly present in the ground-tile fixture validation report, not the three canonical behavior source files. For G13 the instruction says 'Chat in the user's language' and mandates English for technical filenames, identifiers, manifests, schemas and docs; it does not literally promise that every conversation will be Swedish, except when the user's language is Swedish.

| Case | Static source probe | Required ChatGPT host test |
|---|---|---|
| G01 | supported | Distinguish designSheet from production ready |
| G02 | review (128x64 in fixture) | Generate and measure exact diamond geometry and seams |
| G03 | supported | Verify distinct canvases and fixed footprint/anchors |
| G04 | supported | Inspect footprint, anchors, regions and manifests |
| G05 | supported | Validate separate static and animated geometry |
| G06 | supported | Check each direction/state and frame/foot-point consistency |
| G07 | supported | Check ordered frame exports, timing and clipping |
| G08 | supported | Inspect PNG alpha and text-free localization-safe icons |
| G09 | supported | Verify separately exported parallax layers and seams |
| G10 | supported | Reject an invalid presentation sheet |
| G11 | supported | Measure deterministic packing in actual output files |
| G12 | supported | Confirm approved assets unchanged in selective revision |
| G13 | review (equivalent wording) | Swedish chat and English technical output |
| G14 | supported | Verify text-free base art and localized layers |
| G15 | supported | Confirm external SpriteKit/TV/device checks remain unverified |
| G16 | supported | Compare actual prototype and upgraded manifests byte/field-wise |

**Functional test status: all G01–G16 NOT RUN.** None is marked PASS from keyword coverage or packaging checks. There are no actual generated PNGs, frame measurements, runtime screenshots, Xcode or Apple TV records in this run. This report is a test plan plus verifiable source evidence, not a claim of image-generation validation.

## Executed deterministic checks

- `tests/verify_static_contracts.py`: 14 source probes supported, G02/G13 review; all six distribution ZIPs passed CRC checks; per-archive SHA256 hashes in JSON evidence.
- Original GPT Byggaren 1.6.33 `lint_gpt_project.py`: 0 errors, 12 warnings (generated dist and preserved duplicates).
- Original engine `build_distributions.py --version 1.0.0-rc2`: PASS; project and five runtime archives rebuilt.
- Original engine `validate_distributions.py`: PASS after rebuild restored required build directories.
- Original engine `assess_release_readiness.py --include-build-state --json`: `ready_with_warnings`, 0 structural blockers, test-model warning. See `docs/evidence/engine-release-readiness.json`.

## Cross-runtime functional parity requirements

| Capability | ChatGPT Chat | OpenAI Plugin | Claude Projects | Claude Skills | OpenCode |
|---|---|---|---|---|---|
| Canonical behavior packaging | Packaged | Packaged | Packaged | Packaged | Packaged |
| Actual image generation/edit tool | Host test required | Confirm host tool access and image editing path | Confirm externally supported image provider or tool | Confirm external image provider integration | Configure and test compatible image provider/tool |
| Deterministic image processing and PNG measurement | Host test required | Obtain real executable/script tool or adapter | External script execution/adapter | External script execution/adapter | Configure local tool/script execution |
| Manifest, evidence and cumulative ZIP | Host test required | Verify durable artifact and attachments | Verify files and workspace persistence | Verify files and workspace persistence | Verify filesystem access and artifact export |
| End-to-end G01–G16 | Not run | Not run | Not run | Not run | Not run |

Do **not** equate archive creation with execution parity. For each host, verify tool availability, permissions, file attachments, image export, deterministic measurement, source-of-truth ZIP update, and evidence labels. If a host lacks image generation or code/file tooling, a documented external adapter can supply those capabilities, but must itself pass all critical tests before activation. No unsupported provider APIs or adapter implementations are asserted here.

## Production release decision

**NO-GO.** The engine's `ready_with_warnings` is a *structural* result. Image generation, processing, file delivery and G01–G16 remain untested in each target host. First run G01, G02, G11, G12 and G16 with real generated assets in ChatGPT Chat, then the other tests, and repeat with each alternate runtime before claiming full parity.
