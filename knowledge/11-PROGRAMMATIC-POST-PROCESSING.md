# Programmatic Post-Processing

## Purpose

Define tool-agnostic, deterministic processing requirements for converting generated or edited source graphics into measurable runtime assets and manifests.

This file owns crop, padding, alpha cleanup, canvas normalization, anchor alignment, deterministic packing, manifest generation and file inspection. It does not own art direction, asset-family geometry, maturity meanings or release zip handling.

## 1. When deterministic processing is required

Use measured or programmatic processing whenever acceptance depends on exact:

- pixel dimensions;
- canvas dimensions;
- alpha or background transparency;
- crop bounds or padding;
- anchor, baseline or foot-point alignment;
- grid, rows, columns, spacing or margins;
- sheet region coordinates;
- frame order and naming;
- duplicate or missing-file detection;
- manifest agreement with actual files.

Image generation may produce visual source material. It must not be trusted to produce exact runtime geometry without inspecting the resulting file.

## 2. Pipeline stages

Process assets in this order unless a documented exception is required:

1. **Ingest** — inventory source files, preserve originals and record source identity.
2. **Decode and inspect** — confirm format, dimensions, color mode and alpha availability.
3. **Isolate** — separate individual assets from presentation sheets or mixed source art.
4. **Clean** — remove unintended background, guides, labels, separators, halos and debris.
5. **Normalize visual scale** — apply the approved scale reference without changing logical footprint.
6. **Crop content** — calculate content bounds using the declared alpha threshold or mask policy.
7. **Apply padding and canvas** — place content on the exact declared canvas without unintended clipping.
8. **Align anchors** — position foot points, baselines or registration points consistently.
9. **Normalize image mode** — use the required color and alpha representation.
10. **Assemble sheets** — place assets or frames from explicit ordering data, never by visual guess.
11. **Generate manifest** — derive file paths, pixel sizes, regions and frame metadata from produced files and assembly data.
12. **Validate output** — measure the written files, not only in-memory intentions.
13. **Create previews** — generate separate presentation views from runtime output.
14. **Record provenance and changes** — identify source assets and operations used.

## 3. Source preservation and reproducibility

- Keep generated or edited source art in `source/` when delivery scope permits.
- Never destructively replace the only source file before validated output exists.
- Record processing parameters that affect reproducibility: target canvas, scale operation, interpolation, crop threshold, padding, alpha policy, anchor coordinates, packing order and output format.
- Use stable identifiers rather than filenames alone to connect sources, outputs and manifest records.
- A rerun with unchanged source and parameters should produce functionally identical geometry and metadata.

## 4. Isolation and cleanup

Presentation sheets are source or preview material, not runtime sheets. When isolating assets:

- identify the intended asset region explicitly;
- remove headings, captions, decorative frames, dividers, mockup surfaces and watermarks;
- do not erase legitimate semi-transparent effects;
- inspect edges for color contamination or matte halos;
- preserve declared visual overflow;
- reject isolation when asset boundaries cannot be separated reliably without design decisions.

For ambiguous source separation, return `Not verified` or request clarification rather than inventing missing pixels.

## 5. Crop and padding policy

- Crop is based on declared content rules, not arbitrary visual tightness.
- Transparent pixels may be meaningful padding for animation, VFX, anchor stability or consistent sheet cells.
- Alpha threshold, mask and shadow inclusion rules must be declared when they affect bounds.
- Cropping must not change logical footprint.
- Padding must be deterministic and stated per edge or derived from the target anchor/canvas rule.
- After crop and padding, verify no non-transparent pixel lies outside the canvas.

## 6. Canvas normalization

For each asset define or derive:

- target canvas width and height;
- content placement rule;
- anchor or foot-point position;
- permitted visual overflow;
- scale method and interpolation;
- whether source aspect ratio must be preserved.

Do not stretch an asset to fill a canvas unless explicitly approved. Assets sharing a runtime extraction rule must share compatible canvas semantics, not merely similar appearance.

## 7. Alpha and color handling

- Confirm whether the output requires alpha.
- Inspect the written file for a real alpha channel where required.
- A checkerboard shown in a preview is not proof of transparency.
- Remove unintended opaque backgrounds without destroying intentional translucent pixels.
- Detect fully opaque borders, isolated debris and alpha fringes where practical.
- State whether RGB values in fully transparent pixels are normalized when that matters to the target pipeline.
- Avoid silent palette or profile conversions that change approved colors.

## 8. Anchor and frame alignment

Anchors are metadata and a placement operation:

- use the declared normalized or pixel anchor convention consistently;
- translate content so equivalent foot points occupy the same canvas coordinate;
- keep animation registration stable across frames unless motion is intentionally encoded;
- report maximum alignment deviation when measured;
- do not infer gameplay collision from visual bounds or anchors.

For isometric props, validate foot point and logical footprint independently from visual height and overflow.

## 9. Deterministic sheet assembly

A runtime sheet requires explicit assembly data:

- sheet dimensions or a deterministic rule that derives them;
- cell or region dimensions;
- rows and columns where grid-based;
- margins and spacing;
- stable asset or frame order;
- one declared asset per cell or region, unless a documented packed-atlas format is used;
- no accidental overlap;
- region coordinates within sheet bounds;
- compatible canvas and anchor semantics for grid slicing.

Grid sheets and packed atlases are different contracts. Do not describe a packed atlas as a regular grid. Do not mix assets that require incompatible extraction rules unless the manifest fully describes each region.

## 10. Manifest generation

Generate manifest records from actual output and assembly data wherever possible. Do not manually transcribe measurable fields when they can be derived.

For every output record, verify:

- stable ID and source asset ID;
- relative path;
- format;
- actual pixel size;
- alpha presence when relevant;
- canvas size;
- logical footprint and anchor from approved specification;
- sheet region or frame data from assembly results;
- validation check references;
- known limitations and external checks.

Paths must resolve inside the delivery package. IDs must be unique. Every runtime output must have a manifest entry, and every manifest path must identify an existing intended file.

## 11. Inspection of written output

After writing files, reopen and inspect them. At minimum verify:

- file exists and decodes;
- actual format and dimensions;
- expected image mode and alpha;
- non-transparent bounds fit within canvas;
- sheet regions fit within sheet dimensions;
- declared rows, columns, margins and spacing reproduce the regions;
- manifest pixel sizes and paths match;
- expected asset/frame count equals actual count;
- no duplicate IDs, duplicate regions or missing outputs;
- runtime files contain no known presentation elements.

Checks that cannot be executed must remain `Not verified`.

## 12. Scaling and filtering

- Apply scaling only from an approved source-to-target scale rule.
- Pixel-art scaling must use integer factors and nearest-neighbor unless its specialized pipeline explicitly permits otherwise.
- High-resolution art should use the approved resampling method and be inspected for halos, ringing and line-weight changes.
- Do not let post-processing silently compensate for a wrong style scale or camera contract.
- Filtering metadata must describe intended runtime behavior but does not prove renderer behavior.

## 13. Preview generation

Previews are derived presentation artifacts and belong in `preview/`:

- contact sheets may add labels, checkerboards, guides and scale references;
- previews must clearly identify maturity and non-runtime status when ambiguity is possible;
- preview decoration must never be copied into `output/`;
- contact-sheet order should mirror manifest order where useful for review.

## 14. Failure handling and revision scope

Classify processing failures as `technicalExport` unless the root cause is source art, manifest-only or request ambiguity.

When source art is correct, prefer deterministic repair:

- recrop;
- repad;
- realign;
- convert alpha or format;
- rebuild only affected sheets;
- regenerate manifest fields and dependent previews.

When one asset changes, identify all derived sheets, manifests, previews and validation checks that depend on it. Do not rebuild unrelated approved assets unless the packing contract necessarily changes their coordinates; if coordinates change, report that as an interface-impacting revision.

## 15. Minimum processing record

For each processing run, record at least:

- input source identities;
- output identities;
- operation sequence;
- important parameters;
- warnings and assumptions;
- files changed;
- checks executed and evidence locations;
- tool or script version when available.

A processing record may be included in `source/` or `validation/` and must use English technical documentation.
