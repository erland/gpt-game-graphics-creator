# Art Direction and Style Lock

## Purpose

Turn an approved asset brief into a repeatable visual system before expensive production begins. This file owns style exploration, reference interpretation, approval checkpoints and the normative style-lock fields used by all asset pipelines.

## Inputs

Use, in priority order:
1. explicit approved requirements in `ASSET-BRIEF.md` and `ASSET-SPEC.yaml`;
2. an approved `STYLE-GUIDE.md`;
3. supplied references with documented interpretation;
4. existing approved assets in the same series;
5. clearly labelled safe assumptions when the request can proceed without hiding risk.

Never infer gameplay behavior, collision, logical footprint, camera behavior or animation budget from visual references alone.

## Style-development sequence

1. **Extract constraints** — audience, mood, genre, target platform, projection, readability distance, asset maturity and localization boundary.
2. **Interpret references** — record what each reference contributes: palette, composition, shape language, material treatment, lighting, outline, texture, animation feel or density. Also record what must not be copied.
3. **Identify conflicts** — flag incompatible projection, lighting, scale, rendering method or detail density.
4. **Create representative probes** — use the smallest set that tests the highest-risk decisions. Typical probes are one ground tile, one tall prop, one character pose, one UI icon and one effect frame.
5. **Compare probes against the brief** — assess silhouette, readability, contrast, material recognition, scale and technical feasibility.
6. **Lock the direction** — mark the guide `approved` only after the selected direction and unresolved exceptions are explicit.
7. **Propagate the lock** — all later assets inherit the approved values unless a documented exception is approved.

## Required style-lock fields

Define when relevant:
- style status: `provisional`, `approved` or `revisionRequired`;
- visual intent and audience;
- palette roles and contrast hierarchy;
- shape language;
- material rules;
- outline policy;
- lighting direction and intensity hierarchy;
- cast-shadow and contact-shadow policy;
- texture and surface-detail policy;
- detail density by asset class;
- silhouette priorities;
- scale references;
- projection, orientation and camera assumptions;
- edge treatment and anti-aliasing policy;
- rendering pipeline: pixel art, high-resolution raster, vector-like raster or mixed source;
- localization boundary;
- forbidden motifs or treatments;
- approved exceptions.

## Reference safety

References guide attributes, not replicas. Do not reproduce a distinctive copyrighted character, logo, composition, prop or environment merely because it appears in a reference. Combine abstract traits, document transformations and prefer user-owned or rights-cleared sources. Detailed rights rules belong to file 13.

## Approval checkpoints

Use three checkpoints for larger series:
- **Direction checkpoint:** mood, palette, shape language and rendering method.
- **Technical sample checkpoint:** scale, projection, canvas behavior, anchor compatibility and readability.
- **Series checkpoint:** a small cross-section proving that the style survives across asset families.

A provisional guide permits exploration but not broad production. An approved guide permits production. A revision-required guide blocks new series expansion until the conflict is resolved.

## Change control

When the style lock changes:
1. name the changed field;
2. explain why;
3. identify affected assets;
4. preserve unaffected approved assets;
5. decide whether existing assets remain acceptable, require selective revision or invalidate the series sample;
6. version the style guide and delivery.

## Anti-overlap

- Package structure and schemas belong to file 02.
- Maturity thresholds and validation status meanings belong to file 04.
- Asset-family implementation details belong to files 05–10.
- Deterministic image processing belongs to file 11.
