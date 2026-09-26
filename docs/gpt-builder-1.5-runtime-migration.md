# GPT Byggaren 1.5.0 – migreringsplan

Projekt: **Game Graphics Creator**

## Utgångsläge

Projektet är ett fungerande legacy-GPT-projekt med:
- version **1.0.0-rc2**
- huvudinstruktion i `builder/MAIN-INSTRUCTION.md`
- **13 permanenta Knowledge-filer**
- G01–G16 manuella GPT Preview-tester, samtliga `notRun`
- Custom GPT- och Chat ZIP-distribution
- schemas, fixtures och Asset Request/Delivery-kontrakt
- kritiskt beroende av både **Image generation** och **Code Interpreter & Data Analysis**
- privat publiceringsstatus tills Preview-preflight faktiskt har körts och accepterats

## Preserve-first

Migreringen ska bevara:
- instruktionens beteende byte-identiskt tills canonical-källan är etablerad,
- 13/13 aktuella Knowledge-filer,
- Asset Request/Delivery Contract,
- skillnaden mellan visuell kvalitet och teknisk validitet,
- krav på mätning av faktiska filer före tekniska påståenden,
- Image generation för visuell skapande/redigering,
- Code Interpreter/Data Analysis för mätning, post-processing, deterministic assembly, validering och zip-leverans,
- cumulative zip/release workflow,
- VERSION `1.0.0-rc2`,
- G01–G16 som `notRun`,
- `privateUntilPreflight`.

Migreringen får inte markera manuella Preview-tester som körda eller ändra publiceringsstatus.

## Runtime-målbild

### Aktiva baseline-runtimes
1. ChatGPT Chat
2. ChatGPT Custom GPT

### Ska bedömas
- Claude Projects
- OpenCode
- OpenAI Plugin

Ytterligare runtimes får bara aktiveras om de kan uppfylla de kritiska kontrakten för både visuell generering och deterministisk filbearbetning/validering utan att försvaga produktbeteendet.

## Steg

### 1. Baseline och canonical källa
Inför `gpt-project.yaml`, separat migrationsstatus och canonical `assistant/instructions.md` utan beteendeförändring.

### 2. Normalisera GPT Byggaren 1.5-kontrakten
Definiera capability-, artifact-, workspace/state- och tool-kontrakt och lägg maskinell validering.

### 3. Normalisera Chat och Custom GPT
Bygg båda från canonical projektdata och verifiera 13/13 Knowledge samt de kritiska bild-/filverktygsreglerna.

### 4. Bedöm Claude Projects och OpenCode
Gör explicit parity-bedömning för behavior, capability, artifact, workspace/state och tool. Aktivera endast om kritisk parity är verklig.

### 5. Bedöm OpenAI Plugin
Bedöm skills-first-parity för bildflöde, deterministisk post-processing, validering och cumulative zip/state.

### 6. Generalisera build, parity, CI och release
Inför deklarativ runtime-registry och låt aktivt distributionsset härledas därifrån.

### 7. Slutlig readiness och dokumentationssynk
Synka README/release-dokumentation, kör final hygiene och lägg explicit 7/7-migrationsgate.

## Klart-kriterium

Migreringen är klar när:
- canonical beteende är bevarat,
- 13/13 Knowledge är bevarade,
- G01–G16 fortfarande är `notRun`,
- publiceringsstatus fortfarande är privat/preflight-blockerad,
- Chat och Custom GPT verifieras från samma canonical källa,
- övriga runtimes har explicit compatibilitybeslut,
- build/CI/release inte har dolda hårdkodade runtime-antaganden,
- VERSION fortfarande är `1.0.0-rc2`,
- slutlig CI är grön.
