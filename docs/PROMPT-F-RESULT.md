# Prompt F Result — Builder Configuration

## Scope completed

Prompt F implemented the Builder-facing configuration for Game Graphics Creator without adding new asset-production domains.

## Added

- complete Builder field mapping;
- capability recommendations and boundaries;
- machine-readable Builder configuration summary;
- permanent knowledge upload manifest;
- six representative conversation starters;
- profile-image and publication guidance;
- Preview verification checklist;
- capability-use rule in the main instruction.

## Configuration decision

Required capabilities:
- Image generation
- Code Interpreter & Data Analysis

Recommended:
- Web search

Not required in this release:
- Canvas
- Apps
- Custom actions

No fixed recommended model name is stored because model availability can change. The builder should select the strongest currently available compatible model and verify behavior in Preview.

## Deferred

- reference fixtures;
- G01–G15 test pack;
- final preflight and release candidate;
- originality/rights and rendering-specialization knowledge files.
