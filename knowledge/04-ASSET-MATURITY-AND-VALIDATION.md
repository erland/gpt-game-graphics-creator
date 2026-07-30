# Asset Maturity and Validation

## Purpose

Own the maturity model, graphics-side validation statuses, blocking logic, evidence requirements, delivery acceptance and revision triage for all asset families.

This file does not define asset-family geometry or rendering rules. Those remain in files 03 and 05–10. It does not define deterministic image operations; those belong to file 11.

## 1. Maturity is not validation status

Each delivered asset has exactly one maturity value:

- `designSheet` — visual exploration or communication material; not runtime output.
- `prototypeAsset` — usable for prototyping with documented limitations.
- `productionCandidate` — intended for final use and believed complete, but one or more required checks or approvals remain open.
- `productionReady` — all graphics-side blocking requirements have passed, evidence is recorded, no blocking graphics-side issue remains, and the asset has been explicitly accepted for integration.

Validation status is recorded per check and is separate from maturity. A `productionCandidate` can contain many passed checks. A visually polished asset can still be `prototypeAsset`. `productionReady` never means that SpriteKit loading, gameplay collision, TV readability or physical-device behavior has been verified unless those tests were actually performed and recorded.

### Allowed maturity movement

- Promotion requires evidence that the target level's criteria are met.
- Demotion is required when a new blocker invalidates the current maturity claim.
- Revision must preserve the previous maturity only when all requirements supporting that maturity remain valid.
- A package-level label must not silently raise the maturity of individual assets.

## 2. Validation statuses

Every check uses exactly one status:

- `Passed` — the stated requirement was checked against the actual delivered file or authoritative metadata and met.
- `Failed` — the requirement was checked and did not meet the acceptance criterion.
- `Not verified` — the check is relevant but no sufficient test or evidence exists.
- `Not applicable` — the check does not apply to the affected asset or delivery; the reason must be recorded.

`Not verified` is never equivalent to `Passed`. A check may not be marked `Passed` from appearance alone when the requirement concerns dimensions, alpha, grid, frame order, file contents or other measurable properties.

## 3. Requirement identity and traceability

Every validation check must identify:

- a stable check ID;
- the requirement source, such as a request criterion, schema field, style-lock rule or owning knowledge rule;
- the affected asset IDs or package scope;
- the acceptance criterion;
- status;
- whether failure is blocking;
- evidence or reason;
- external owner when the check cannot be performed by Game Graphics Creator.

A requirement must not be rewritten during validation to make an output pass. Ambiguous requirements are classified as request ambiguity and resolved through the handoff contract.

## 4. Graphics-side validation domains

Use only the domains relevant to the asset:

1. **File and format** — expected file exists, opens, uses the declared format and contains no unintended presentation material.
2. **Dimensions and canvas** — exact pixel size, canvas size, cell size, margin, spacing and sheet bounds.
3. **Alpha and background** — transparency requirement, alpha mode, no unintended opaque background or alpha fringe.
4. **Crop and padding** — no unintended clipping, required padding retained, visual overflow represented as declared.
5. **Alignment and anchors** — anchors, foot points, baselines and frame alignment are consistent with the contract.
6. **Manifest consistency** — IDs, paths, pixel sizes, regions, frame data and validation references match actual files.
7. **Sheet integrity** — deterministic ordering, unique regions, no overlap unless declared, no missing or duplicate entries.
8. **Visual consistency** — approved palette, projection, scale, lighting, silhouette, material and detail-density rules.
9. **Animation stability** — identity, frame count, order, timing, foot point, clipping, loop or one-shot behavior.
10. **Tile behavior** — declared edge matching, adjacency, diamond consistency, orientation coverage and region geometry.
11. **Localization separation** — language-neutral base art and separately managed localized text where required.
12. **Package integrity** — required package files exist and preview files are separated from runtime output.

## 5. Blocking criteria

A failed or unverified check is blocking when it prevents reliable use at the declared maturity or violates a non-negotiable contract. Typical blockers include:

- missing runtime file;
- wrong dimensions, grid, spacing or margins where deterministic slicing is required;
- missing or incorrect alpha where transparency is required;
- clipped required content;
- manifest regions that do not match the actual file;
- duplicate IDs, missing entries or ambiguous frame ordering;
- wrong projection, footprint or anchor when these affect placement;
- missing required direction, state or frame;
- presentation text, guides, separators, frames, watermarks or mockup background in runtime output;
- an unresolved critical request decision;
- a `productionReady` claim with relevant graphics-side checks marked `Not verified`.

A non-blocking issue may remain only when the declared maturity permits it, it is documented in `knownLimitations`, and it does not invalidate the asset's intended use.

## 6. Overall status

Derive package or asset overall status mechanically:

- `Failed` when any blocking check is `Failed`.
- `Not verified` when no blocking check failed but at least one required blocking check is `Not verified`.
- `Passed` when every required blocking check is `Passed` or justified `Not applicable`.

Non-blocking failures must still be reported. They do not turn the overall status into `Passed` without qualification; the report summary must state that acceptance is maturity-limited or conditional.

## 7. Evidence policy

Good evidence includes:

- measured image dimensions and mode;
- alpha-channel inspection results;
- computed sheet coordinates and bounds;
- hash or file identity when useful;
- manifest-to-file comparison;
- pixel-edge comparison for tile seams;
- frame-to-frame anchor or silhouette measurements;
- a recorded human approval for explicitly visual criteria.

Screenshots and visual previews may support visual review but do not prove exact dimensions, alpha, cropping or sheet geometry. Generated claims without inspection are not evidence.

## 8. Developer-side and external checks

When unavailable, mark these as `Not verified` with an external owner rather than guessing:

- SpriteKit loading and atlas behavior;
- gameplay collision and logical interaction;
- camera and depth-sorting behavior in the actual game;
- filtering and scaling behavior in the target renderer;
- TV readability and safe-area behavior on the target display;
- Xcode, tvOS and physical Apple TV verification;
- final legal or rights approval.

External checks do not automatically block graphics-side `productionCandidate`. They do block claims that those external behaviors are verified.

## 9. Validation report rules

`validation/VALIDATION-REPORT.md` is the human-readable report. Machine-readable validation data must conform to `contract/schemas/validation-report.schema.yaml` when included.

The report must contain:

- package identity and version;
- scope and files inspected;
- overall status and maturity impact;
- assumptions and unresolved questions;
- check table with IDs, sources, affected assets, status, blocking flag and evidence;
- failures grouped by category: visual, technical export, manifest or request ambiguity;
- external checks;
- revision recommendation;
- explicit statement of what was not verified.

## 10. Revision triage and selective regeneration

For each failed check:

1. link it to the exact requirement;
2. classify it as `visual`, `technicalExport`, `manifest`, or `requestAmbiguity`;
3. identify affected asset IDs and derived files;
4. determine whether source regeneration is necessary;
5. preserve all unaffected approved assets;
6. rerun every check whose evidence could have been invalidated;
7. update manifest, validation report, package version and changelog.

Prefer the smallest valid revision scope:

- metadata-only correction when pixels are correct;
- deterministic re-export when source art is correct but canvas, alpha, crop, alignment or packing is wrong;
- selective asset regeneration when visual source content is wrong;
- full-series regeneration only when a shared style lock, scale, projection or source dependency changed.

Never regenerate approved assets merely for visual variety during a corrective revision.

## 11. Acceptance rules by maturity

### Design Sheet

Requires clear presentation labeling and must not be placed in runtime output. Technical runtime checks are normally `Not applicable`.

### Prototype Asset

Must be structurally usable for its declared prototype purpose. Known limitations and all unverified production requirements must be documented.

### Production Candidate

Must pass all graphics-side blockers that can be verified in the current environment. Remaining external checks and any human art approval must be explicit.

### Production Ready

Requires:

- all applicable graphics-side blocking checks `Passed`;
- manifest and actual files consistent;
- no unresolved critical request ambiguity;
- no hidden known blocker;
- recorded acceptance for subjective visual criteria;
- external checks accurately separated rather than implied.

If these conditions are not met, use `productionCandidate` or lower.
