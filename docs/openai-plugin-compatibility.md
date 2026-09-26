# OpenAI Plugin – compatibility assessment

Projekt: **Game Graphics Creator**  
GPT Byggaren: **1.5.0**

## Slutsats

OpenAI Plugin bedöms som **reduced**, **advisory-only** och lämnas **inte aktiv**.

Game Graphics Creator kräver en sammanhängande pipeline där följande fungerar tillsammans:

1. faktisk **Image generation** för visuell skapande/redigering,
2. faktisk filinspektion och mätning,
3. deterministisk post-processing och sheet assembly,
4. manifest- och validation report-generering,
5. cumulative zip-workflow med senaste kompletta godkända arkiv som source of truth.

Pluginens skills/reference-material kan bära instruktion, metoder, contracts och checklistor, men full runtime-parity kan inte garanteras för hela denna kedja utan ytterligare runtime-/tool-stöd.

## Parity-bedömning

| Område | Bedömning |
|---|---|
| Behavior | reduced |
| Capability | reduced |
| Artifact | reduced |
| Workspace/state | reduced |
| Tool | reduced |

### Behavior

Instruktioner om asset workflow, art direction, maturity, validation och revision kan uttryckas som skills. Men canonical-beteendet kräver att faktiska bilder skapas och därefter tekniskt verifieras; detta får inte reduceras till textbaserad rådgivning.

### Capability

Kritiska capabilities:
- `image_generation`
- `code_interpreter_and_data_analysis`

Båda behövs i samma produktflöde. En plugin som endast kan beskriva eller orkestrera processen utan garanterad tillgång till motsvarande verktyg är inte equivalent.

### Artifact

Schemas, YAML, Markdown, manifests och validation reports kan representeras. Visuella source assets, runtime assets och färdiga zip-leveranser måste däremot kunna skapas och valideras med riktig evidence.

### Workspace/state

För längre arbeten är senaste kompletta godkända arkiv samt aktuell brief/spec/manifest/validation-data auktoritativa. Chatthistorik eller plugin-session får inte ensam vara source of truth.

### Tool

Plugin v1 får inte kringgå canonical tool-boundaries:
- ingen falsk Image generation,
- ingen påstådd filinspektion utan faktisk filåtkomst,
- ingen teknisk validitetsstatus utan mätbar evidence,
- ingen release-/zip-status utan faktiskt skapad och validerad artefakt.

## Aktiveringsbeslut

- status: `assessed_not_active`
- compatibility: `reduced`
- advisory_only: `true`
- blockers:
  - `critical_image_generation_not_guaranteed`
  - `deterministic_file_pipeline_not_guaranteed`
  - `persistent_delivery_state_not_guaranteed`

Ingen Plugin-distribution byggs eller publiceras i denna migrering.

## Framtida omprövning

Plugin kan omprövas när runtime kan uppfylla samma canonical kontrakt för:
1. faktisk Image generation,
2. faktisk filinspektion/mätning,
3. deterministisk post-processing och assembly,
4. manifest + validation evidence,
5. cumulative zip-workflow,
6. persistent projekt-/leveransstate,
7. ärlig failure/status-rapportering.

Ingen canonical produktregel ändras av denna bedömning.
