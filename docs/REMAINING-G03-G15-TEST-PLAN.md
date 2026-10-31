# Remaining G03–G10 and G13–G15 functional verification plan

This plan uses the authoritative descriptions in `tests/G03.md` … `tests/G10.md` and `tests/G13.md` … `tests/G15.md`. No test outcome is upgraded by this plan.

## Execution priority

| Test | Priority | Automation boundary | Required host evidence |
|---|---|---|---|
| G10 — Reject presentation sheet | P1 | Automated pixel/layout check plus host refusal | presentation-only,runtime-export-rejected |
| G15 — Honest external verification | P1 | Automated assertions and host transcript review | NOT_VERIFIED |
| G03 — Props with differing canvas heights | P1 | Automate dimensions, footprint, anchor validation | footprint-stable,canvas-distinct |
| G04 — Multi-tile structures | P1 | Automate region rectangles / occupancy; host review | footprint-2x2,regions-declared |
| G05 — Static tiles vs animated effects | P1 | Automate separate atlas grouping or reject mixed sheet | separate-layout |
| G13 — Swedish chat, English docs | P1 | Transcript inspection and schema language guard | swedish-chat,english-contract |
| G06 — Character directions/states | P2 | Automate cardinality, file existence and foot points; host identity check | complete-matrix |
| G07 — Animation consistency | P2 | Automate clip bounds, anchor, order, fps and looping declaration | frame-order,timing |
| G08 — Transparent UI icons | P2 | Automate RGBA/alpha; manual symbol inspection | transparent,text-free |
| G14 — Localized Swedish game text | P2 | Automate separate artwork/text-layer files and locale manifest | separate-text-layer |
| G09 — Parallax layers | P3 | Automate width/height, layer separation and edge comparison | layer-separation,seam-evidence |

## Test strategy

**P1: deterministic contract and negative testing (G10, G15, G03, G04, G05, G13).** Validate manifest/layout constraints and whether the assistant refuses unsupported runtime claims. Start with G10 to detect false acceptance of an attractive but invalid sheet; follow with G15 to verify honest verification status.

**P2: richer output contracts (G06, G07, G08, G14).** Validate matrix completeness, frame metadata, alpha and text-layer separation. Inspect generated images or clips manually for visual continuity and localization quality; do not substitute a JSON check for visual proof.

**P3: multilayer runtime integration (G09).** Test layered PNG dimensions and declared seams programmatically, then run a real scroll/camera integration for the full parallax result.

## Fixture model

`tests/e2e/remaining/remaining-test-cases.json` defines **synthetic scenarios** with test prompts, expected machine-checkable contract fields and negative-case checks. This is test data, not real passing asset output. `test_remaining_fixtures.py` validates internal fixture consistency and the presence of original case definitions; it does not perform image generation or claim host tests passed.

## Test execution protocol

1. In a separate test chat, attach the current E2E source fixtures and choose a case from P1 to P3; explicitly invoke the installed Game Graphics Creator 1.2.1 Skills.
2. Produce actual image/manifest output when the case requires it. Save the original prompt, files and independent SHA-256 calculations.
3. Run deterministic checks against produced bytes (canvas, RGBA, alpha, atlas rectangles, layout, frame counts, layers and hashes as applicable).
4. Record model-generated appearance, text placement, visual identity and animation review separately from technical assertions.
5. Mark individual checks PASS, FAIL, NOT_VERIFIED or NOT_APPLICABLE with evidence path and host/tool attribution; never promote an entire test to PASS from schema validity alone.
6. Do not change source test statuses to PASS without test execution and preserved evidence.

## Existing approval context and release limits

G01, G02, G11, G12, G16 have scoped technical ChatGPT-session acceptance documented in `docs/evidence/ACCEPTANCE-G01-G02-G11-G12-G16-1.2.1.md`. This does not prove independent Plugin runtime execution or complete G01–G16 coverage. The eleven cases listed here are **NOT RUN**. No full five-runtime parity is claimed. Production Ready and public production release remain **NO-GO** until visual approval, real graphics generation/export and relevant host checks have been evidenced.
