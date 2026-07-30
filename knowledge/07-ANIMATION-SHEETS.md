# Animation Sheets

## Purpose

Define frame continuity, timing metadata, state/direction organization and clean runtime delivery for animated sprites and effects. Visual-effect design specifics belong to file 10.

## Animation contract

For each animation declare:
- owner asset or character;
- state;
- direction when applicable;
- frame count;
- ordered frame identifiers;
- fps or per-frame durations;
- loop or one-shot behavior;
- event or contact frames when requested;
- canvas and anchor convention;
- output grouping.

Do not change frame budget, state list, direction list, timing or loop behavior without approval.

## Continuity rules

Across frames preserve:
- character or effect identity;
- scale;
- anchor and foot point;
- stable camera and projection;
- intentional volume and silhouette changes;
- consistent lighting and palette;
- clean temporal progression.

Motion may move around the anchor only when the contract intends root motion or an offset sequence. Otherwise eliminate accidental jitter.

## Contact and action readability

For locomotion, identify contact, passing and lift phases as needed. For attacks or interactions, ensure anticipation, action and recovery are readable within the approved frame budget. Do not add gameplay timing claims that the request does not define.

## Sheet organization

Use a deterministic organization such as:
- one state/direction per sheet;
- compatible states in fixed rows;
- compatible directions in fixed rows or columns;
- individual frames plus generated sheets.

Whichever strategy is used, document ordering and extraction. Separate animations with incompatible canvas, anchors, frame size or playback semantics.

## Preview versus runtime

A labelled contact sheet, animated preview or montage belongs in `preview/`. Runtime sheets contain only extractable frames. Do not include state labels, arrows, timelines, separators or decorative framing in runtime output.

## One-shot effects

For one-shot sequences, declare the terminal behavior: remove, hold final frame, hide or hand control back to the developer. This is delivery metadata, not a claim that game integration was tested.

## Family-specific review checks

Check:
- expected frame count and order;
- stable anchor or explicitly declared offsets;
- no duplicate, missing or swapped frames;
- no clipped motion extremes;
- stable identity and scale;
- loop seam quality where looping is required;
- timing metadata completeness;
- clean separation between preview and runtime assets.

Formal validation statuses belong to file 04. Deterministic alignment and packing belong to file 11.
