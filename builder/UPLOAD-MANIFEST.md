# GPT Builder Upload Manifest

## Upload policy

The Builder supports a limited permanent knowledge set. Upload normative reference files only. Behavior, priorities and global rules remain in `MAIN-INSTRUCTION.md`.

## Upload now

Upload these 13 files in numeric order:

1. `knowledge/01-ROLE-AND-RESPONSIBILITY.md`
2. `knowledge/02-ASSET-REQUEST-AND-DELIVERY-CONTRACT.md`
3. `knowledge/03-ART-DIRECTION-AND-STYLE-LOCK.md`
4. `knowledge/04-ASSET-MATURITY-AND-VALIDATION.md`
5. `knowledge/05-TILESETS-AND-TILEMAP-ASSETS.md`
6. `knowledge/06-SPRITES-AND-CHARACTER-SETS.md`
7. `knowledge/07-ANIMATION-SHEETS.md`
8. `knowledge/08-ISOMETRIC-ASSETS.md`
9. `knowledge/09-UI-ICONS-AND-SIGNAGE.md`
10. `knowledge/10-VFX-BACKGROUNDS-AND-PARALLAX.md`
11. `knowledge/11-PROGRAMMATIC-POST-PROCESSING.md`
12. `knowledge/12-ZIP-WORKFLOW-AND-RELEASE.md`
13. `knowledge/13-PROTOTYPE-TO-PRODUCTION-ART.md`

## Add in later prompts

Reserve upload slots for:

14. `knowledge/14-ORIGINALITY-REFERENCES-AND-RIGHTS.md`
15. `knowledge/15-PIXEL-ART-PIPELINE.md`
16. `knowledge/16-HIGH-RESOLUTION-2D-PIPELINE.md`

The planned final knowledge set therefore remains below the 20-file limit.

## Do not upload as permanent knowledge

- `knowledge/00-KNOWLEDGE-MANIFEST.md` — architecture documentation for maintainers.
- `contract/schemas/*` — distribute inside working request/delivery packages when needed.
- `contract/templates/*` — provide or copy as task fixtures rather than permanent knowledge.
- `docs/PROMPT-*-RESULT.md` — implementation history only.
- `docs/CHANGELOG.md` — release history only.
- `docs/RELEASE-CHECKLIST.md` — maintainer checklist.
- `docs/FILE-OWNERSHIP-AND-ANTI-OVERLAP.md` — maintainer architecture guidance.
- `README.md`, `VERSION` — package metadata.

## Builder field mapping

| Builder field | Source file |
|---|---|
| Name | `NAME.txt` |
| Description | `DESCRIPTION.md` |
| Instructions | `MAIN-INSTRUCTION.md` |
| Conversation starters | `CONVERSATION-STARTERS.md` |
| Capabilities | `CAPABILITIES.md` |
| Knowledge | This upload manifest |

## Verification after upload

In GPT Preview, confirm that the GPT:

1. uses the main instruction for behavior rather than quoting architecture files;
2. retrieves the correct asset-family file for the request;
3. does not invent missing schemas or rights rules;
4. can create downloadable files when Code Interpreter & Data Analysis is enabled;
5. can generate or edit images when Image generation is enabled;
6. reports unavailable capabilities honestly instead of pretending they ran.


## Preview-only support files
`fixtures/` and `tests/` are retained in the project/release package for Preview testing. They are not normative knowledge files unless a specific test requires temporary upload.
