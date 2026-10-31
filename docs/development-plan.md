# Migreringsplan — GPT Byggaren 1.6.33

1. **Inventering (klar):** bevarade originalfiler, migreringsrapport och 13 Knowledge-filer.
2. **Projektmodell (grund klar):** canonical instruktion bevarad; modulär Skill-uppdelning uppskjuten till ett granskat separat beslut.
3. **Motor (klar):** installerad och självtestad originalmotor 1.6.33.
4. **Distributioner (klar på paketnivå):** Chat och projekt-ZIP byggda och validerade. Fyra andra runtime-mål förblir blockerade; inga påståenden om funktionsparitet.
5. **Hygien (klar):** dokumentation och CI uppdaterade, äldre skript och historik inventerade, hänvisningar granskade. Se `STEP-5-HYGIENE-REPORT.md`.
6. **Slutverifiering (återstår):** kör G01–G16 i faktisk värd, testa bildgenerering, bildbearbetning, ZIP/filpipeline och återupptagning. Aktivera enbart runtimes som verkligen verifieras. Publicera först efter särskilt godkännande.
