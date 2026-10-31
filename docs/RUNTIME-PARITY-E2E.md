# Functional parity requirements after ChatGPT fixture harness

| Runtime | Unverified integration and required next proof |
|---|---|
| ChatGPT Chat | Run prompts G01/G02/G11/G12/G16; export real PNG/manifests and record visual/integration approvals independently |
| OpenAI Plugin | Verify access to image generation/editing tool, Python/Pillow-equivalent deterministic work, writable artifact storage, attachment transfer, ZIP output, and state retention |
| Claude Projects | Supply and test a compatible image-generation provider and deterministic file/ZIP runner; inspect attachment workflows and source instruction equivalence |
| Claude Skills | As above, plus confirm Skill activation, reference loading, script execution rights, and compatible file paths |
| OpenCode | Configure image-provider adapter and local filesystem/Pillow-capable scripts; validate file I/O permissions, command run and artifact export |

Packaging success does not imply hosted functional parity. To reach parity, rerun the same real-file verifier on *outputs from each runtime*, then validate visual quality, style fidelity, and game integration with human/engine tests. No runtime host test was executed in this package.
