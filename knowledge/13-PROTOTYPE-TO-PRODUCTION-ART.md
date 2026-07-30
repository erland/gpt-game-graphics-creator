# Prototype-to-Production Art Workflow

## Purpose

This file defines how the GPT moves from simple, technically useful prototype graphics to polished production-oriented art without breaking approved runtime contracts.

## Production mode

`productionMode` is separate from asset maturity and validation status. It describes the intended visual-production phase:

- `technicalPrototype` — simple, readable runtime-oriented graphics used to prove geometry, footprint, anchors, states, sheets and integration assumptions.
- `visualPrototype` — exploratory art that tests style, silhouette and readability but may still change technically or visually.
- `productionArt` — polished art created under an approved style lock and intended for final use, subject to validation and integration checks.
- `visualUpgrade` — replacement or refinement of an existing approved prototype while preserving declared technical contracts unless an explicit contract change is approved.

A technically valid prototype is not automatically polished production art. Polished art is not automatically Production Ready.

## Default inference

When the user emphasizes footprints, anchors, manifests, grids, validation or integration but supplies no approved style guide or explicit production-art request, default to `technicalPrototype` and state that assumption before substantial production.

Do not stop for clarification when this is a safe, reversible assumption. Do not silently present schematic prototype graphics as final art.

When the user explicitly requests polished, final, game-ready, production-quality, hand-painted, pixel-art or otherwise styled runtime assets, use `productionArt` or `visualUpgrade` as appropriate.

## Prototype quality requirements

Technical prototypes must still be intentional and useful references. Preserve:

- stable asset identity and naming;
- recognizable object category and primary silhouette;
- orientation and facing;
- approximate scale and proportions;
- logical footprint and base placement;
- anchor or foot point;
- important functional visual cues;
- state, direction and frame contracts when relevant.

Avoid unnecessary detail that increases revision cost. Prototype assets may be vector-like or schematic, but they must remain clean, coherent and suitable for integration testing.

## Visual upgrade contract

A visual upgrade must preserve these fields unless the request explicitly authorizes a contract change:

- asset ids and source relationships;
- logical footprint;
- projection and orientation;
- tile diamond and scale reference;
- anchor or foot point;
- state names and direction names;
- frame count, frame order and timing contract;
- atlas group, filenames and manifest relationships;
- declared localization boundaries.

Canvas size or visual overflow may change only when the updated manifest, packing and depth-sorting assumptions remain compatible or the change is explicitly approved.

## Upgrade workflow

1. Identify the approved prototype delivery and source version.
2. Record the locked technical contract for each affected asset.
3. Confirm or establish the production-art style lock.
4. Create one or more representative upgraded samples.
5. Compare prototype and upgraded assets for identity, footprint, anchor, projection, scale and contract compatibility.
6. Obtain visual approval when the user requests review before the full series.
7. Upgrade only the approved scope.
8. Normalize and pack output deterministically.
9. Regenerate manifests and validation evidence from actual written files.
10. Run regression checks against the locked prototype contract.
11. Report any approved contract changes separately from visual changes.

## Source categories

Distinguish:

- `conceptReference` — inspiration or direction; not necessarily exact or approved.
- `approvedStyleReference` — approved visual rules or representative art.
- `upgradeSource` — material explicitly chosen as the source for runtime-art replacement.
- `runtimeOutput` — normalized and packaged files intended for integration.

Do not treat a labeled contact sheet, generated mood image or presentation graphic as a runtime source merely because it looks polished.

## Validation additions

For `visualUpgrade`, include regression evidence for all locked technical fields. Use `Failed` when an unapproved visual change breaks a locked contract. Use `Not verified` when the check requires developer-side runtime evidence.

A delivery must state its production mode in README and manifests. If a package mixes modes, declare the mode per asset and summarize the package intent.
