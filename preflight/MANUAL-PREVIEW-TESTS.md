# Manual GPT Preview Tests

Run every case in `tests/G01.md` through `tests/G15.md` after configuring the GPT. Preserve prompts, responses, generated files and screenshots as evidence where relevant.

| Test | Primary purpose | Manual reason | Release blocking |
|---|---|---|---|
| G01 | Design Sheet maturity labeling | Requires observing GPT behavior | Yes |
| G02 | Exact isometric ground-tile request | Requires tool output and actual-file inspection | Yes |
| G03 | Same footprint, different canvas heights | Requires manifest/canvas behavior | Yes |
| G04 | Multi-tile structures and manifest | Requires package-generation behavior | Yes |
| G05 | Static tiles separated from animated effects | Requires pipeline routing behavior | Yes |
| G06 | Character directions and states | Requires identity/state consistency review | Yes |
| G07 | Animation frame consistency | Requires visual and technical frame review | Yes |
| G08 | Transparent UI icon sheet | Requires actual alpha/output review | Yes |
| G09 | Background and parallax package | Requires layer/package review | Yes |
| G10 | Reject presentation sheet as runtime tileset | Requires refusal/correction behavior | Yes |
| G11 | Deterministic sheet assembly and manifest | Requires Code Interpreter/file inspection | Yes |
| G12 | Selective regeneration | Requires revision behavior across turns | Yes |
| G13 | Swedish chat, English technical files | Requires language-boundary observation | Yes |
| G14 | Localizable Swedish game text | Requires localization-boundary observation | Yes |
| G15 | Honest SpriteKit verification status | Requires claim-boundary observation | Yes |

## Acceptance rule

A test passes only when its expected behavior is met and none of its listed failure conditions occur. Missing evidence or unavailable capabilities must be recorded as `Not verified`, never converted to `Passed`.
