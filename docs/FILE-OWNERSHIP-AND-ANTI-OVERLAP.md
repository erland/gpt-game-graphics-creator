# File Ownership and Anti-Overlap Rules

## Global ownership

### Main instruction
Owns:
- identity;
- global mission;
- responsibility boundary;
- universal workflow;
- universal honesty and validation behavior;
- language rules;
- high-level maturity concepts.

Must not contain:
- full schemas;
- long per-asset procedures;
- detailed zip commands;
- full test cases;
- repeated examples from knowledge files.

### 01 — Role and Responsibility
Owns:
- detailed responsibility boundary;
- collaboration boundary with developer GPTs;
- decision authority and escalation behavior.

### 02 — Asset Request and Delivery Contract
Owns:
- package structures;
- schemas;
- required and optional fields;
- handoff lifecycle;
- contract validation.

### 03 — Art Direction and Style Lock
Owns:
- brief interpretation;
- style exploration;
- reference handling;
- style-lock fields;
- approval checkpoints.

### 04 — Asset Maturity and Validation
Owns:
- maturity definitions;
- validation statuses;
- blocking criteria;
- validation report structure;
- acceptance logic.

### 05 — Tilesets and Tilemap Assets
Owns tile geometry, sheet slicing semantics, tile adjacency, wall/edge roles, prop grouping and multi-tile structure rules.

### 06 — Sprites and Character Sets
Owns character identity, proportions, states, directions, mirroring, equipment consistency and sprite-set canvas strategy.

### 07 — Animation Sheets
Owns temporal continuity, frame order, timing metadata, loop behavior and runtime animation-sheet organization.

### 08 — Isometric Assets
Owns shared isometric projection, tile diamond, foot-point conventions, visual overflow, orientation and graphics-side depth metadata.

### 09 — UI, Icons and Signage
Owns screen-space readability, icon families, UI states, signage and localization separation.

### 10 — VFX, Backgrounds and Parallax
Owns effect-specific metadata, background crop/safe-area behavior, and independently usable parallax layers.

Files 05–10 must not redefine global package schemas, validation status meanings, maturity levels or responsibility boundaries.

### 11 — Programmatic Post-Processing
Owns:
- deterministic crop, alpha, alignment, normalization, packing and inspection;
- when generated images require measured correction;
- tool-agnostic processing requirements.

### 12 — Zip Workflow and Release
Owns:
- safe archive inspection and unpacking;
- source-of-truth selection;
- isolated working-copy behavior;
- conservative cleanup;
- cumulative release packaging and fresh-extraction verification;
- changelog, version and release-note requirements.

### 13 — Originality, References and Rights
Will own:
- reference-use boundaries;
- originality expectations;
- rights-safe documentation;
- prohibited copying behavior.

### 14–15 — Rendering pipeline specializations
Own:
- pixel-art-specific rules;
- high-resolution 2D-specific rules.

They may specialize shared pipeline rules but must not duplicate the common foundation.

## Anti-overlap tests

Before adding content to a file, ask:
1. Is this a global rule? Put it in the main instruction or role file.
2. Is this a data contract or schema? Put it in file 02.
3. Is this a validation definition? Put it in file 04.
4. Is this unique to one asset family? Put it in the relevant pipeline file.
5. Is this deterministic file processing? Put it in file 11.
6. Is this release packaging? Put it in file 12.
7. Is this only an example? Keep it in fixtures or tests, not as duplicated normative text.

## Conflict resolution

Priority order:
1. explicit user-approved requirement;
2. request/delivery contract;
3. main instruction;
4. owning knowledge file;
5. asset-specific example;
6. safe assumption clearly marked as an assumption.

When two permanent files conflict, update the owning file and replace duplicate text in the other file with a short reference.

- `knowledge/13-PROTOTYPE-TO-PRODUCTION-ART.md` owns production-mode semantics and prototype-to-polished-art regression rules. Other files may reference but not redefine these modes.
