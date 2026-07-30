# Asset Request and Delivery Contract

## Purpose

This file defines the normative handoff between a requesting game-design/development workflow and Game Graphics Creator. It owns package structure, contract lifecycle, required fields, assumption handling and delivery completeness. Asset-family files may add stricter requirements but must not redefine this contract.

## Contract principles

1. Treat the latest complete request package as the request source of truth.
2. Do not infer gameplay contracts such as collision, logical footprint, interaction behavior, states or camera changes when they are absent.
3. Distinguish blocking omissions from non-blocking omissions.
4. Use the smallest safe assumption only when work can continue without concealing integration risk.
5. Record every accepted assumption and every unresolved question.
6. Keep preview material separate from runtime output.
7. A delivery package is not complete until its manifest and validation report describe the actual output files.
8. Never claim that a schema-valid package is visually approved, technically integrated or Production Ready merely because its structure is valid.

## Asset Request Package

Canonical structure:

```text
asset-request/
├── README.md
├── ASSET-BRIEF.md
├── ASSET-SPEC.yaml
├── STYLE-GUIDE.md
├── VALIDATION-CRITERIA.md
└── references/
```

### File ownership

- `README.md` — package identity, version, request owner, intended consumer, package status and file inventory.
- `ASSET-BRIEF.md` — visual purpose, player-facing context, asset families, desired mood, priorities and exclusions.
- `ASSET-SPEC.yaml` — machine-readable technical asset declarations and shared defaults.
- `STYLE-GUIDE.md` — approved or provisional style lock, palette, lighting, projection, shape language and reference interpretation.
- `VALIDATION-CRITERIA.md` — acceptance criteria, blocking checks and external developer-side checks.
- `references/` — supplied visual or technical references with provenance and usage notes.

### Minimum request metadata

A request package must declare:

- `packageId`;
- `packageVersion`;
- `requestStatus`;
- `requestedMaturity`;
- at least one asset entry;
- a stable unique `id` and `assetType` for every entry;
- enough information to identify the intended output and whether the request is exploratory or runtime-oriented.

For runtime-oriented requests, each asset must also declare or explicitly defer the relevant technical contract, such as canvas, footprint, anchor, projection, frame structure, transparency or localization behavior.

### Request statuses

- `draft` — incomplete and expected to change.
- `readyForReview` — requester believes the package can be checked.
- `approvedForProduction` — requester has approved the declared contract for production work.
- `revisionRequested` — an earlier delivery exists and specified changes are requested.

`approvedForProduction` does not mean the requested assets are Production Ready. It only means the request contract is approved for execution.

## Intake procedure

On receipt, perform these checks in order:

1. Inventory all files and identify the latest complete package.
2. Parse `ASSET-SPEC.yaml` and verify schema compliance where possible.
3. Compare README, brief, specification, style guide and validation criteria for contradictions.
4. Classify each missing or conflicting decision as blocking, non-blocking or external.
5. Produce an intake summary before substantial production begins.
6. Proceed only under an explicit contract state.

## Contract states

- `Accepted` — sufficient and internally consistent for the requested work.
- `Accepted with assumptions` — work can proceed with documented non-blocking assumptions.
- `Blocked` — one or more unresolved decisions would require inventing gameplay, integration or identity-critical rules.
- `Revision intake` — request targets an earlier delivery and preserves unaffected approved assets.

## Blocking decisions

A decision is blocking when proceeding would require one of the following:

- inventing gameplay behavior, collision or interaction logic;
- inventing a logical footprint that affects placement or pathing;
- changing approved projection, camera, direction count, state list or frame budget;
- guessing runtime slicing where cells, margins, ordering or regions are ambiguous;
- guessing visible language when text must be baked into an asset;
- replacing a locked visual identity without approval;
- overwriting or discarding approved source assets without an explicit revision scope.

## Safe assumptions

A safe assumption must be:

- reversible;
- low-impact;
- clearly documented;
- compatible with supplied requirements;
- isolated from gameplay and integration contracts.

Examples include using a provisional filename convention, placing preview-only notes in documentation, or choosing a lossless working format when no export format is yet mandated. Assumptions must not silently become approved requirements.

## Asset specification model

The canonical schema is `contract/schemas/asset-request.schema.yaml`.

The shared package section may define defaults. Each asset entry overrides defaults explicitly. Relevant fields include:

- identity: `id`, `assetType`, `requestedMaturity`, `description`;
- geometry: `canvasSize`, `logicalTileSize`, `logicalFootprint`, `visualBounds`, `anchorPoint`, `visualOverflow`;
- view: `projection`, `orientation`, `directions`;
- rendering: `transparentBackground`, `alphaPolicy`, `palette`, `lightingDirection`, `outlinePolicy`, `shadowPolicy`;
- animation: `states`, `frameCount`, `frameOrder`, `fps`, `loop`;
- packaging: `grid`, `spacing`, `margin`, `atlasGroup`, `outputMode`;
- runtime constraints: `filtering`, `scaling`, `localizationConstraints`;
- acceptance: `acceptanceCriteria`, `externalChecks`.

Omit irrelevant fields rather than using invented values. Use `null` only when the schema permits an explicitly unresolved value and record why it remains unresolved.

## Asset Delivery Package

Canonical structure:

```text
asset-delivery/
├── README.md
├── preview/
├── output/
│   ├── individual/
│   └── sheets/
├── manifest/
│   ├── assets.yaml
│   └── ASSET-MANIFEST.md
├── validation/
│   └── VALIDATION-REPORT.md
└── source/
```

### Delivery ownership

- `README.md` — delivery identity, source request, version, scope, assumptions, known limitations and inventory.
- `preview/` — contact sheets, annotated views and presentation images; never treated as runtime assets.
- `output/individual/` — clean individual runtime-oriented exports.
- `output/sheets/` — clean deterministic sheets or atlas source sheets.
- `manifest/assets.yaml` — machine-readable record of actual delivered files, dimensions, regions and technical metadata.
- `manifest/ASSET-MANIFEST.md` — human-readable summary of the machine-readable manifest.
- `validation/VALIDATION-REPORT.md` — requirement-by-requirement status with evidence and external checks.
- `source/` — editable or intermediate source material approved for inclusion.

### Runtime-output purity

Files under `output/` must not contain:

- headings or captions;
- measurement guides or grid labels;
- decorative borders or mockup frames;
- code, prompts or explanatory prose;
- watermarks;
- preview-only backgrounds;
- unintended natural-language text.

Such material belongs in `preview/` or documentation.

## Delivery manifest

The canonical schema is `contract/schemas/asset-delivery-manifest.schema.yaml`.

Every runtime file must have a manifest entry. Each entry must identify:

- stable asset `id`;
- asset type and maturity;
- relative output path;
- file format;
- measured pixel dimensions;
- alpha/transparency status when relevant;
- canvas, anchor and footprint when relevant;
- sheet region, cell or frame data when packed;
- source request asset id;
- validation summary;
- known limitations and external checks.

The manifest describes actual files, not intended files. Missing output must not be represented as delivered.

## Validation report contract

The report must use only:

- `Passed`;
- `Failed`;
- `Not verified`;
- `Not applicable`.

`Not verified` never counts as passed. Each check must include:

- requirement id or source;
- status;
- evidence or reason;
- affected asset ids;
- blocking or non-blocking classification;
- owner of any remaining external check.

Detailed maturity and validation semantics are owned by file 04 when implemented. Until then, this contract defines only the required report structure and allowed statuses.

## Delivery completeness levels

- `Structural draft` — package structure exists, but output or reports may be incomplete.
- `Review delivery` — intended assets and previews are present for visual/technical review.
- `Revision delivery` — scoped changes are delivered and unaffected approved files are preserved.
- `Release candidate delivery` — graphics-side checks are complete or explicitly marked; package is ready for developer integration testing.

These are package states, not asset maturity levels.

## Revision handoff

A revision request must identify:

- source delivery id and version;
- affected asset ids;
- failed requirements or requested visual changes;
- assets that must be preserved;
- whether manifest regions or filenames may change;
- expected version increment.

The revised delivery must update README, manifest and validation report. Unaffected approved assets should remain byte-identical when practical.

## Versioning

Use semantic package versions where practical:

- patch — corrections that preserve the approved contract and identifiers;
- minor — added assets or compatible contract extensions;
- major — incompatible identifier, geometry, sheet-layout or contract changes.

Every delivery must reference the request package id and version it implements.

## Conflict priority

When request files conflict, use this priority only after reporting the conflict:

1. explicit user-approved clarification;
2. latest approved `ASSET-SPEC.yaml`;
3. `VALIDATION-CRITERIA.md` for acceptance behavior;
4. approved `STYLE-GUIDE.md` for visual rules;
5. `ASSET-BRIEF.md` for intent;
6. README metadata;
7. documented safe assumption.

Do not silently resolve a material contradiction by priority alone. Record the conflict and its resolution.
