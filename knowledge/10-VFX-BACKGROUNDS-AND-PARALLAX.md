# VFX, Backgrounds and Parallax

## Purpose

Define separate production rules for visual effects, static backgrounds and parallax layers. These assets may share style direction but have different runtime geometry and playback behavior.

## VFX pipeline

For each effect declare:
- purpose and visual priority;
- world-space or screen-space use;
- projection and orientation when world-space;
- source point or anchor;
- footprint or influence area only when supplied by the request;
- frame count, order, timing and loop behavior;
- additive, alpha or other blend expectation when known;
- canvas and overflow policy;
- color variants or intensity tiers.

Effects must communicate the requested event without falsely implying gameplay radius, damage, collision or timing that was not approved.

Keep particles, flashes and trails within the declared canvas or document intended overflow. Separate effects with incompatible canvases or blend assumptions.

## Background pipeline

Backgrounds must declare:
- target aspect ratio and minimum dimensions;
- crop and safe-area behavior;
- camera movement assumptions;
- horizon and focal-region constraints;
- whether the image tiles, extends or crops;
- foreground readability requirements;
- text-safe regions when requested.

Avoid high-contrast detail behind important gameplay or UI regions unless the brief requires it.

## Parallax pipeline

Each parallax layer must be independently usable and declare:
- layer ID and depth order;
- intended movement ratio or qualitative depth class when supplied;
- transparency policy;
- edge-extension or tiling behavior;
- overlap needed for camera movement;
- shared horizon and lighting alignment;
- target viewport and overscan.

Do not flatten layers into one background when separate runtime layers were requested. Do not invent movement ratios if they affect integration; mark them developer-side or request approval.

## Seamless and extended assets

For horizontally or vertically repeating layers, ensure edge continuity and avoid unique landmarks that reveal repetition too quickly unless intended. For non-repeating extended scenes, provide enough overscan for the declared camera range.

## Localization

Keep language-dependent signs, billboards and labels separate from backgrounds when possible. Use text-free environmental bases and optional localized overlays.

## Preview versus runtime

Composite scene previews may demonstrate the combined effect but belong in `preview/`. Runtime output contains separate clean effect frames, backgrounds and parallax layers.

## Family-specific review checks

For VFX, check sequence continuity, anchor stability, clipping, frame order, blend assumptions and loop seam. For backgrounds, check dimensions, crop safety, focal hierarchy and foreground readability. For parallax, check layer separation, transparency, edge behavior, shared horizon and sufficient overscan.

Formal status assignment belongs to file 04. Deterministic frame and layer processing belongs to file 11.
