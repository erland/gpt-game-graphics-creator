# Steg 5 — dokumentation, CI och filhygien (2026-10-31)

## Beslut

- `README.md`, `PROJECT.md`, `STATUS.md`, migrationsplan och checklista synkroniseras med steg 4:s faktisk byggda Chat-/projektpaket.
- CI använder den installerade kanoniska 1.6.33-motorns `scripts/build_distributions.py` och `scripts/validate_distributions.py` och kräver PyYAML. Ingen dynamisk `main`/`latest`-motor eller egen byggare.
- CI körs på push, pull request och manuellt; publiceringsjobbet för historisk 1.5-release har avaktiverats. CI-artefakter är temporära och märkta **unreleased**. Release kräver särskilt beslut efter G01–G16.
- `migration/legacy-1.5-scripts/` bevarar originalbyggaren och validatorn för jämförelse, inte aktiv körning. Övriga historiska 1.5-valideringsskript finns kvar under `scripts/` som referenser och har **inte** bevisats utbytbara; inga av dem raderas.
- Den gamla runtime-registry-filen, migrationsrapport, Buildermaterial och äldre dokumentation bevaras för spårbarhet. Inga förändringar i canonical instruktionsbeteende, Knowledge, fixtures eller tester.
- `dist/` byggs om från aktuell källa och ska inte versionshanteras. Cache och OS-metadata utesluts ur källarkivet.

## Kända avgränsningar

Paketvalidering testar inte bildgenerering eller filpipeline. Fyra alternativa runtime-mål är avstängda. Manuell Preview G01–G16 kvarstår. Äldre duplicerade Markdown-mallar behålls med varning. Ingen automatisk release.

## Verifieringsutfall

- Kanoniskt bygge och distributionsvalidering: **PASS** efter ombyggnad. Validatorn kräver den genererade `build/chat`-katalogen under kontrollen; den behöver inte ingå i den levererade käll-ZIP:en.
- Lint efter borttagna Python-cachefiler och genererad `build/`: **0 fel, 8 varningar** (fyra dist-artefakter och fyra grupper av duplicerade Markdown-filer enligt lint). Kända varningar är icke-blockerande.
- Projekt-ZIP ompaketeras från arbetskopian utan `build/` och cache, med kompletta `dist/`-arkiv; CRC kontrolleras.
