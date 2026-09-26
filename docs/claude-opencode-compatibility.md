# Claude Projects och OpenCode – runtime compatibility

Projekt: **Game Graphics Creator**  
GPT Byggaren: **1.5.0**

## Slutsats

Både Claude Projects och OpenCode bedöms som **reduced** och lämnas **inte aktiva** i denna migrering.

Game Graphics Creator har två kritiska runtime-krav som måste fungera tillsammans:

1. **Image generation** för faktisk visuell skapande/redigering.
2. **Deterministisk filbearbetning och validering** för mätning, alpha-inspektion, crop/pad/normalize, ankare, sheet assembly, manifest och zip-leverans.

En runtime som endast klarar den ena halvan ger inte full produktparity.

## Parity-bedömning

| Område | Claude Projects | OpenCode |
|---|---|---|
| Behavior | reduced | reduced |
| Capability | reduced | reduced |
| Artifact | reduced | reduced |
| Workspace/state | equivalent | equivalent |
| Tool | reduced | reduced |

### Claude Projects

Textinstruktion, knowledge, asset contracts och projektfiler kan representeras. Däremot kan projektets kombinerade krav på faktisk bildgenerering och den deterministiska filpipeline som canonical-kontraktet kräver inte behandlas som garanterat equivalent.

Beslut:
- compatibility: `reduced`
- activation: `not_active`
- blocker: `critical_visual_and_file_pipeline_not_guaranteed`

### OpenCode

OpenCode är väl lämpat för workspace, filer, scripts och deterministisk validering. Det räcker ändå inte för full parity eftersom konstnärlig Image generation är en separat kritisk capability och inte får ersättas av kodgenererad grafik.

Beslut:
- compatibility: `reduced`
- activation: `not_active`
- blocker: `critical_image_generation_not_guaranteed`

## Artifact-parity

Markdown, YAML, schemas, manifests, validation reports och zip-paket kan representeras i båda kandidaterna. De visuella source assets som ska skapas eller redigeras genom riktig Image generation är däremot en obligatorisk del av produktens arbetsflöde.

Tekniska påståenden om bildfiler får dessutom bara göras efter faktisk inspektion/mätning. Ingen runtime får degradera detta till antaganden.

## Workspace/state

Båda kandidaterna kan arbeta med projektfiler och strukturerat state. Denna del bedöms därför som equivalent. Det räcker dock inte för aktivering när en kritisk capability eller tool-chain fortfarande är reducerad.

## Aktiveringsregel

En runtime får aktiveras först när den kan uppfylla samtliga följande samtidigt:

1. faktisk konstnärlig bildgenerering/redigering,
2. faktisk filinspektion,
3. deterministisk post-processing och sheet assembly,
4. manifest- och validation report-generering,
5. cumulative zip-workflow med senaste kompletta godkända arkiv som source of truth,
6. inga falska integrations- eller validation claims.

Ingen canonical produktregel ändras av denna bedömning.
