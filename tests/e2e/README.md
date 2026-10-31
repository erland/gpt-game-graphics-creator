# Executable e2e-fixture harness

Requires Python 3.10+ and Pillow (`python -m pip install Pillow`). All supplied PNGs are deliberately synthetic fixture examples.

- Run deterministic byte/manifest/atlas checks: `python tests/e2e/verify_png_manifests.py --output docs/evidence/e2e-fixture-verification.json`
- Run positive and negative automated tests: `python -m unittest discover -s tests/e2e -p 'test_*.py' -v`
- Follow `CHATGPT-E2E-RUNBOOK.md` for *actual* ChatGPT host tests.

The supplied positive fixture is NOT evidence that the host generated any image. An actual host output must be saved separately and tested independently. G01 and visual approval/integration need human review.
