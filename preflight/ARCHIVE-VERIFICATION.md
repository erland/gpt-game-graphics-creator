# Archive Verification

The release archive for `1.0.0-rc1` was created from the preflight-passed working tree.

Final packaging verification includes:

- one intended top-level directory;
- archive entry review;
- zip integrity test;
- fresh extraction into a clean directory;
- rerun of required-file, version, instruction-size and knowledge-count checks against the extracted copy.

Result: **Passed**.

The archive hash is reported alongside the downloadable release and is intentionally not embedded here, because embedding it would change the archive itself.
