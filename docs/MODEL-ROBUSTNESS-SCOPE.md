# Scope of the engine model robustness validator

`validate_model_robustness.py` is a GPT Byggaren *builder workflow* policy validator. It requires builder-specific states (`idea_analysis`, `architecture`, `planning`, etc.), `build_claude_skills_zip`, and builder-specific compatibility eval scenarios. This Game Graphics Creator assistant is not the GPT Byggaren assistant; it uses a domain-specific game asset production workflow.

**Disposition:** `MODEL-ROBUSTNESS-001` remains NOT APPLICABLE to this assistant's behavior contract, not PASS. We do not inject a fictitious builder state machine or change its canonical instructions merely to satisfy an unrelated validator. Instead, release gating must include its own G01–G16 real-host evaluations, which remain NOT RUN, and actual image/file runtime tests. If the engine adds a general-purpose model robustness validator, use that later.
