# UI, Icons and Signage

## Purpose

Define screen-space UI assets, icons, indicators and in-world signage with strong readability and a clear localization boundary.

## UI families

Separate, when relevant:
- interface chrome and panels;
- buttons and controls;
- status indicators and meters;
- inventory or ability icons;
- cursors and selection markers;
- controller prompts;
- logos and title treatments;
- in-world signs and symbols.

Do not combine incompatible target sizes or scaling rules into one undifferentiated sheet.

## Readability

Design for the declared display size and viewing distance. Check silhouette, contrast, negative space and state distinction at actual target size, not only enlarged preview size. Decorative detail must not obscure function.

## States

Declare required states such as normal, focused, highlighted, pressed, selected, disabled, warning or cooldown. State changes must remain distinguishable under the intended contrast and accessibility constraints.

## Icons

Each icon should have:
- a single primary meaning;
- a stable visual family;
- declared canvas and safe area;
- consistent optical scale;
- transparent background unless otherwise specified;
- naming that describes function rather than visual guesswork.

Avoid relying only on color where state or meaning must remain accessible.

## Localization boundary

Prefer text-free icons and separate text layers. Do not bake natural-language labels into UI sheets or environmental signs when localization may be needed. When visible game text is explicitly requested:
- keep editable source separate;
- declare language and fallback behavior;
- provide text-free base assets when practical;
- do not claim font or glyph coverage beyond what was checked.

Symbols that are culturally specific or ambiguous must be documented rather than assumed universal.

## Controller and platform prompts

Use generic action semantics unless platform-specific glyphs are explicitly requested and rights or platform rules are satisfied. Do not claim platform compliance merely because a glyph looks familiar.

## Runtime output

Runtime UI sheets contain only usable assets. Labels, dimensions, usage notes and comparison layouts belong in `preview/` or documentation.

## Family-specific review checks

Check:
- legibility at target size and distance;
- consistent optical scale and safe area;
- distinct required states;
- transparent edges without halos;
- no unintended baked text;
- language variants and text-free bases are separated;
- filenames and manifest IDs describe function clearly.
