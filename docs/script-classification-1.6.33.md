# Script classification — migration stage 3

| Script | Classification | Decision |
|---|---|---|
| `scripts/build_distributions.py` | Build tooling | Replaced by original 1.6.33 engine; 1.5 copy preserved |
| `scripts/validate_distributions.py` | Validation tooling | Replaced by original 1.6.33 engine; 1.5 copy preserved |
| `scripts/validate_gpt_builder_1_5_contract.py` | Legacy test | Retained for regression; not runtime tool |
| `scripts/validate_gpt_builder_1_5_migration.py` | Legacy migration test | Retained for regression; not runtime tool |
| `scripts/validate_runtime_distribution_registry.py` | Build validation | Retained; not runtime tool |
| `scripts/validate_claude_opencode_compatibility.py` | Compatibility validation | Retained; not runtime tool |
| `scripts/validate_openai_plugin_compatibility.py` | Compatibility validation | Retained; not runtime tool |

The canonical behavior is still `assistant/instructions.md`. A modular Skill architecture is **not activated**: a separate behavioral responsibility decomposition and traceability review is required before altering the authoritative instruction. Runtime tools: none of the above scripts is promoted.
