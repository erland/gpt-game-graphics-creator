# GPT Builder Configuration

## Name

Game Graphics Creator

## Description

Creates, structures, validates and revises technically usable graphics for 2D and isometric games, including sprites, tilesets, animation sheets, props, VFX, UI assets, backgrounds and parallax layers. Works from a visual and technical brief, preserves style consistency, and delivers clean runtime assets with manifests and honest validation status.

## Instructions

Paste the complete contents of `MAIN-INSTRUCTION.md` into the GPT Builder Instructions field.

## Conversation starters

Use the starters in `CONVERSATION-STARTERS.md`. They deliberately cover creation, review, package construction, style locking, deterministic export and selective revision.

## Recommended capabilities

Enable:

- **Image generation** — required for creating and editing visual source assets and design explorations.
- **Code Interpreter & Data Analysis** — required for inspecting dimensions and alpha, deterministic cropping and canvas operations, sheet assembly, manifest generation, archive handling and downloadable file creation.

Enable when available and useful:

- **Web search** — useful for current technical references, public-domain or licensed-reference discovery, and external documentation. It must not replace user-provided briefs or silently introduce unverified rights assumptions.

Leave disabled by default:

- **Canvas** — not required for the core asset workflow. It may be enabled if the builder prefers an additional long-form editing surface, but the GPT must still produce files and packages through the defined workflow.
- **Apps** — no app dependency is defined in this release.
- **Custom actions** — no external API contract is defined in this release.

## Recommended model

Do not hard-code a model name in this package. Select the strongest currently available model that supports the enabled image-generation and data-analysis capabilities. Verify the choice in GPT Preview because model availability can vary by account, workspace and region.

## Knowledge uploads

Upload only the files marked `UPLOAD` in `UPLOAD-MANIFEST.md`. Do not upload schemas, templates, changelogs, prompt-result reports or release checklists as permanent knowledge unless later Preview testing demonstrates a specific retrieval need.

## Profile image

Use a simple original icon that reads clearly at small size: a clean game-asset sheet or isometric tile combined with a precise grid motif. Avoid logos, copyrighted characters, embedded text and visually dense contact-sheet layouts.

## Sharing and publication

Keep the GPT private during Preview testing. Expand visibility only after the required G01–G16 regression cases have been run and accepted. Do not describe the GPT as production verified before that point.
