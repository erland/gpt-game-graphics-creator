# Sprites and Character Sets

## Purpose

Define identity, pose, direction and state consistency for individual sprites and character sprite sets. Animation timing and runtime animation-sheet layout belong to file 07.

## Character identity lock

Before producing a multi-state set, establish:
- canonical proportions and scale;
- silhouette-defining features;
- palette and material assignments;
- face, hair, clothing and equipment rules;
- left/right asymmetry;
- foot-point convention;
- direction model;
- state inventory;
- permitted deformation and exaggeration.

Use a neutral turnaround or representative pose set when direction consistency is a material risk.

## Directions

Directions must be explicit, for example `south`, `southWest`, `west`, `northWest`, `north`, `northEast`, `east`, `southEast`. Do not silently substitute mirrored directions when asymmetric equipment, lighting or readable handedness makes mirroring invalid.

Document whether:
- each direction is unique;
- some directions are mirrored;
- lighting remains world-relative or character-relative;
- weapon hand, insignia or accessories must switch or remain fixed.

## States

Treat states as approved contracts. Do not invent, remove, merge or rename gameplay states to simplify production. For each state, declare the required directions, pose intent and whether it is static or animated.

Examples include idle, walk, run, attack, interact, hurt, defeated and carry, but only requested states are normative.

## Consistency rules

Across the set, preserve:
- apparent body height and mass;
- canonical equipment and costume details;
- palette assignments;
- foot point and ground contact;
- direction-specific silhouette;
- outline and lighting behavior;
- intended camera projection;
- readable separation from the background.

Perspective or foreshortening may change visible proportions, but must remain explainable by the locked projection rather than identity drift.

## Canvas strategy

Choose one of these and document it:
- common canvas for compatible sprites;
- per-state canvas with shared anchor metadata;
- individual files normalized later into runtime groups.

Do not crop tightly around each pose when that would cause anchor jitter or incompatible frame geometry.

## Equipment and modular parts

When bodies, equipment or costumes are modular, define:
- shared attachment anchors;
- layering order;
- compatible states and directions;
- occlusion rules;
- whether pieces are exported combined or separately.

Do not claim arbitrary interchangeability unless the combinations were designed and checked.

## Family-specific review checks

Check:
- identity is stable across states and directions;
- scale and ground contact are consistent;
- no required direction or state is missing;
- asymmetry and mirroring rules are respected;
- extremities and equipment are not unintentionally clipped;
- filenames and manifest identifiers map unambiguously to character, state and direction.

Animation continuity checks belong to file 07. Measured normalization belongs to file 11.
