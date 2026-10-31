# Game Graphics Creator — projektmodell (GPT Byggaren 1.6.33)

Syfte: specificera, skapa och validera grafik för 2D- och isometriska spel.

## Källor och kontrakt

- `assistant/instructions.md`: auktoritativt beteende, oförändrat.
- `builder/MAIN-INSTRUCTION.md`: äldre originalinstruktion, bevarad.
- `knowledge/`: 13 permanenta filer enligt `builder/UPLOAD-MANIFEST.md`.
- `contract/`, `fixtures/`, `tests/`: artefaktkontrakt och G01–G16.
- `gpt-project.yaml`: aktiv 1.6.33-profil och runtime-switchar.
- `scripts/` och `templates/`: installerad originalmotor 1.6.33.

## Beslut och verifieringsgränser

Chat och projektarkiv byggdes och paketvaliderades i steg 4. Övriga fyra runtime-mål är explicit inaktiverade och har inte byggts. Custom GPT är endast historisk kompatibilitet. Ingen host-testad bildgenerering eller filpipeline; publicering blockerad. Steg 5 synkroniserar dokumentation och CI utan att ändra domänbeteende eller versionsnumret `1.0.0-rc2`. Modulär Skill-arkitektur är fortfarande ej godkänd.
