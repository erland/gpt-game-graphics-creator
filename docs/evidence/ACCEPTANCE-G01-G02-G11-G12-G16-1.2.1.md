# ChatGPT-session acceptance evidence — Game Graphics Creator 1.2.1

Five supplied acceptance archives were inspected as ZIP files (CRC/integrity); SHA-256 digests below identify the exact externally supplied evidence packages. The archives are **not committed** to this source repository. Source of evidence: user-provided test-session deliverables, not an independent Plugin runtime.

| Case | Technical scope accepted in ChatGPT session | Remaining NOT VERIFIED | Evidence ZIP SHA-256 |
|---|---|---|---|
| G01 | Design Sheet classification; fixture PNG dimensions and hashes | Separate Plugin runtime, human art approval, developer integration | `58f79598530f2b33ae5bbf09f089c7f4e340d03d2684ad8d0e6cbcf50ae57083` |
| G02 | 128×64 RGBA, isometric diamond mask, sheet and manifest | Seamless tileability, human art approval, engine integration | `d6ff61c7165301cc316859888ff44e37ee21b138a113a718ebef187a2bdbe32c` |
| G11 | 388×66 deterministic assembly, exact pixels, hashes and transparent gutters | Independent Plugin run, engine integration | `f0f654604168102def337ef314d61cddb8a4cbeaf6f5663400babac19409d21f` |
| G12 | One-asset selective revision, unchanged prop bytes, atlas regions and manifests | Independent Plugin run, engine integration | `47907a5a302049dbad7d4be1c2c43a423bbe7524707951fbf5505966e6551ac6` |
| G16 | Locked asset IDs, projection, footprint, anchors, canvas, deterministic atlas, hashes, maturity | Allowed visual changes, animation, localization, approval, engine and independent Plugin run | `81a6f5e22be44385cfbfed77aac244ba4a3aa8a8c54f4b2ee4cdd83a81b08738` |

**Interpretation:** Each listed test was accepted **within its verified technical scope**; this is not a claim that every test has complete coverage, that the Plugin was executed independently, or that production release criteria are met.

## Corrections

- G12 example fixture `selective-revision-manifest.json` now points `prop-01` to the original `prop-prototype.png` with original hash, while only `ground-01` points to the revision. Test fixture revision version is `0.1.1` relative to prototype `0.1.0`.
- G16 now has `tests/e2e/fixtures/G16-verification-contract.json`, expressly declaring missing animation/localization baselines and visual approval. These remain NOT VERIFIED rather than being inferred as preserved.

## Release decision

**NO-GO for Production Ready or full cross-runtime parity.** Five scoped technical tests accepted in a ChatGPT session; G03–G10 and G13–G15 have no acceptance evidence here. Image-model creation, independent Plugin runtime, other host environments, and graphics engine integration remain unverified. Packaging / build status must be evaluated separately on the PR CI run. No production claim is made by these tests.
