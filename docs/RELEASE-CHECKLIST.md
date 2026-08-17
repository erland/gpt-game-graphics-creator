# Release Checklist

Use this checklist for each cumulative GPT package release.

## Intake and source

- [ ] Original input archive preserved unchanged.
- [ ] Archive paths inspected for traversal, absolute paths and unsafe links.
- [ ] Latest complete approved archive identified as source of truth.
- [ ] Input structure and unusually large files inventoried.
- [ ] Conflicting archives or loose files resolved or documented.

## Working copy

- [ ] Changes made in a separate working directory.
- [ ] Requested scope and protected files identified.
- [ ] Approved unrelated assets preserved.
- [ ] Generated outputs rebuilt only where required.

## Package maintenance

- [ ] `VERSION` updated.
- [ ] README current status and setup guidance reviewed.
- [ ] Material release changes are documented in the Git commit/release description.
- [ ] Knowledge manifest and ownership documentation updated when relevant.

## Validation

- [ ] Required files present.
- [ ] Main instruction below 8,000 characters.
- [ ] Permanent knowledge-file count at or below 20.
- [ ] YAML/JSON parsed successfully where applicable.
- [ ] Templates validate against schemas where applicable.
- [ ] Version references agree.
- [ ] No cache, OS metadata, temporary files or nested old releases included.
- [ ] Changed runtime output validated under files 04 and 11 when applicable.

## Archive verification

- [ ] Archive contains one intended top-level project directory.
- [ ] Archive entry list reviewed.
- [ ] Archive integrity test passed.
- [ ] Fresh extraction succeeded.
- [ ] Structural checks rerun against fresh extraction.
- [ ] Final filename clearly identifies stage and version.
- [ ] Remaining external or manual checks documented.
