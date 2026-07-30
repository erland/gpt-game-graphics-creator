# Zip Workflow and Release

## Purpose

Define the safe, cumulative workflow for receiving a request or prior project as a zip archive, modifying it without losing approved material, validating the result, and returning one complete release archive.

This file owns archive handling, source-of-truth selection, working-copy discipline, cleanup, versioning and release packaging. It does not redefine asset schemas, visual pipelines, graphics validation statuses or deterministic image-processing rules.

## Core principles

1. Treat an archive as untrusted input until its paths and contents have been inventoried.
2. Never edit the only copy of the received archive in place.
3. Use the latest complete, user-approved archive as the source of truth.
4. A new release is cumulative unless the user explicitly requests a patch-only package.
5. Preserve approved assets and unrelated files.
6. Remove generated clutter only when it is reproducible or explicitly obsolete.
7. Validate the files that will actually be placed in the final archive.
8. Do not claim archive integrity, schema validity or runtime readiness without performing the relevant check.
9. Return one clearly named complete zip and summarize material changes and remaining external checks.

## Archive intake

### 1. Preserve the original

Keep the received archive unchanged. Record its filename and, when available, version, checksum and receipt date in the work record.

### 2. Inspect paths before extraction

Reject or quarantine archives containing unsafe entries, including:

- absolute paths;
- parent-directory traversal such as `../`;
- paths that escape the intended extraction root;
- device files, sockets or unexpected links;
- ambiguous duplicate paths caused by case-only differences when the target filesystem is case-insensitive.

Symlinks must not be followed outside the extraction root. When link handling is not required, omit links from the working copy and report that decision.

### 3. Inventory before modification

Inventory at least:

- top-level directories;
- version and release metadata;
- builder files;
- knowledge files;
- schemas and templates;
- source assets;
- runtime output;
- previews;
- validation reports;
- unusually large files;
- duplicate or apparently historical exports.

Do not infer that the newest timestamp is the newest valid release. Prefer explicit version metadata and package completeness.

## Selecting the source of truth

Use the latest complete archive that the user supplied or explicitly approved.

A candidate archive is complete only when it contains the project structure needed for the requested work and is internally consistent enough to continue. A newer partial export, isolated output folder or loose file does not replace a complete project archive unless the user explicitly says it should.

When several archives conflict:

1. prefer the user's explicit selection;
2. otherwise prefer the highest valid semantic version with the expected project structure;
3. preserve newer loose assets as review inputs rather than silently overwriting the project;
4. document unresolved conflicts instead of merging by guesswork.

## Working-copy discipline

1. Extract into a new, dedicated work directory.
2. Keep the extraction root separate from the original archive and final release location.
3. Confirm the expected project root; avoid accidental double nesting.
4. Make changes only in the working copy.
5. Do not rename stable public identifiers, asset IDs or contract paths unless the change is required and documented.
6. Preserve file permissions only when they are meaningful and safe; scripts that must be executable should remain executable.
7. Keep temporary files outside the project tree whenever practical.

## Change scope

Before modification, identify:

- requested changes;
- files likely to be affected;
- files that must remain untouched;
- generated outputs that must be rebuilt;
- manifests, reports, versions and documentation that must be updated.

Use the smallest valid change scope. Do not regenerate or replace approved assets merely because a release is being repackaged.

## Cleanup policy

Remove from the final release when safe:

- operating-system metadata such as `.DS_Store` and `Thumbs.db`;
- editor swap and backup files;
- temporary extraction folders;
- caches;
- build logs that are not part of required evidence;
- duplicate intermediate exports;
- obsolete historical release archives nested inside the project;
- reproducible generated files explicitly superseded by the current output.

Do not remove:

- source assets needed for revision;
- the current runtime output;
- schemas, manifests or validation evidence;
- approved references that the project contract requires;
- licensing or attribution files;
- the current changelog or version metadata;
- files whose purpose is uncertain.

If cleanup may be destructive, retain the files and flag them for review.

## Versioning

Use semantic-style project versions unless the project defines another scheme:

- patch: corrections that do not change the public contract or intended asset behavior;
- minor: additive capabilities, new knowledge modules, new asset families or backward-compatible contract extensions;
- major: incompatible contract, path, identifier or workflow changes.

For staged GPT construction, the release may also include a stage suffix or changelog heading such as `0.5.0-prompt-e`, while the machine-readable `VERSION` file should remain unambiguous.

Update all active version references in the same working copy. Do not leave README, changelog and `VERSION` disagreeing.

## Release documentation

Every cumulative release should contain or update:

- `VERSION`;
- `README.md` with current stage and next intended stage;
- `docs/CHANGELOG.md`;
- a stage result or release note describing implemented scope;
- the knowledge manifest when knowledge files changed;
- relevant manifests and validation reports when assets changed.

The release note should distinguish:

- added or changed behavior;
- intentionally deferred work;
- checks actually performed;
- checks not performed or external to the graphics package.

## Validation before packaging

Run checks appropriate to the changed scope. At minimum:

1. verify required project files exist;
2. verify the main instruction remains within the Builder limit;
3. count permanent knowledge files against the configured limit;
4. parse machine-readable YAML or JSON files where tooling is available;
5. validate templates against schemas when the package includes both;
6. inspect referenced output paths and filenames;
7. check for unsafe archive paths and unwanted nested archives;
8. check for temporary, cache and OS metadata files;
9. check that version references and changelog agree;
10. verify the final archive can be listed and extracted without errors.

When asset output changed, also apply the validation and written-file inspection rules owned by files 04 and 11.

A successful zip test proves archive readability, not visual correctness, schema correctness, SpriteKit loading or physical-device integration.

## Deterministic archive creation

Create the final archive from the cleaned project root, not from a parent directory containing work files.

The archive should contain one stable top-level project directory. Use a clear filename such as:

`game-graphics-creator-gpt-prompt-e-v0.5.0.zip`

Avoid embedding absolute paths, temporary directories or the previous release zip. Preserve empty directories only when they communicate required package structure, such as `output/individual/` or `references/`.

When reproducibility matters, normalize file ordering and timestamps where tooling permits. Do not claim byte-for-byte reproducibility unless it was verified.

## Post-package verification

After writing the archive:

1. list its entries;
2. test archive integrity;
3. extract it into a fresh verification directory;
4. rerun critical structural checks against that extracted copy;
5. confirm there is exactly one intended project root;
6. confirm no source archive, work folder or unrelated file was included;
7. record archive size and, when useful, a checksum.

Only the verified archive should be delivered.

## Release result statuses

Use these release-level descriptions without replacing graphics validation statuses:

- `Package verified` — archive integrity and defined structural checks passed;
- `Package verified with unverified external checks` — package checks passed, but developer-side or device checks remain;
- `Package blocked` — a required file, schema, version, archive-integrity or source-of-truth issue prevents release.

Do not use `Package verified` to imply that every contained asset is Production Ready.

## Revision from a returned delivery

When a user returns a prior delivery zip with feedback:

1. select that complete archive as the new baseline unless a newer approved archive exists;
2. map feedback to requirements and affected files;
3. preserve accepted files;
4. revise only the necessary source, output, metadata and reports;
5. increment the version;
6. update changelog and validation evidence;
7. package and verify a new complete archive.

## Failure handling

Stop release and report clearly when:

- no complete source archive can be identified;
- archive paths are unsafe;
- required project files are missing;
- schema or template validation fails for required content;
- version metadata is contradictory;
- the final archive cannot be extracted cleanly;
- requested cleanup would require guessing which source files are obsolete.

Provide the smallest actionable correction. Do not silently construct missing project history or declare a partial package complete.
