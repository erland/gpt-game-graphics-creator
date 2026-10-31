# Skill contract compatibility – GPT Byggaren 1.6.33

The engine ships `schemas/skill-contract.schema.json` for a distinct canonical skill-contract object that requires `contract_version`, `schema`, `mode`, and `definitions`. The modular project config used by the same engine uses `enabled`, `resource_policy`, and `definitions`. The two root formats are incompatible, and substituting one for the other changes the build contract.

This project therefore explicitly selects `schemas/game-graphics-modular-skills.schema.json` through `skills.schema`. The project schema preserves strict validation (`additionalProperties: false`), requires enabled=true and resource_policy=explicit, and reuses the unaltered original engine schema's definition item constraints. The engine's own schema is retained unchanged. Neither Skill contents nor the original instruction have been edited.

Re-check schema compatibility whenever upgrading the engine.
