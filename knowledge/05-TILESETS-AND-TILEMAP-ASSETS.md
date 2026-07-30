# Tilesets and Tilemap Assets

## Purpose

Define production rules for ground tiles, wall or edge tiles, props used with tilemaps, multi-tile structures and runtime tile sheets. This file owns tile-family geometry and slicing semantics, but not general isometric projection rules.

## Core rule

A visually arranged image is not automatically a tileset. A runtime sheet must have declared geometry, ordering and extraction rules that can be verified from the actual output file.

## Required decisions

For each tile asset or compatible group, declare as relevant:
- tile or cell size;
- sheet rows and columns;
- margin and spacing;
- cell or region ordering;
- asset identifier per cell or region;
- logical footprint;
- anchor or foot point;
- visual bounds and overflow;
- transparent-background policy;
- orientation variants;
- adjacency or edge role;
- atlas group and output mode.

## Ground tiles

Ground tiles must:
- use the declared tile geometry;
- preserve seamless shared edges where tiling is intended;
- avoid unintended transparent seams, halos or background contamination;
- keep texture frequency and contrast compatible with gameplay readability;
- declare whether rotation or mirroring is permitted rather than assuming it.

Create explicit variants when directional lighting, markings, wear or edge features make rotation invalid.

## Walls and edges

Walls, fences, cliffs, shorelines and similar edges must declare:
- supported orientations;
- interior/exterior or near/far side where relevant;
- cap, straight, corner, junction and end-piece roles;
- base alignment and overlap behavior;
- whether adjacent pieces share pixels, overlap or merely touch.

Do not infer missing topology variants from a presentation sheet.

## Props and tilemap objects

A prop may share a logical footprint with other props while using a different canvas height. Do not force tall and short props into a common fixed cell unless the extraction contract supports their canvases and anchors. Prefer individual files or compatible subgroups when geometry differs.

## Multi-tile structures

Declare the full logical footprint, the anchor reference cell and any occupied-cell map. A `2x1` object is not a `1x1` object with visual overflow when it actually occupies two logical cells. Decorative overhang may exceed the footprint, but gameplay occupancy remains an approved request-side decision.

## Runtime sheet grouping

Group only assets with compatible:
- projection and orientation;
- cell or extraction geometry;
- anchor convention;
- alpha and filtering policy;
- scale and rendering pipeline.

Normally separate ground tiles, variable-height props, multi-tile structures and animated effects when their canvas or extraction rules differ.

## Ordering

Use a deterministic, documented order such as row-major with explicit IDs. Empty cells must be declared as empty. Multi-cell regions must identify their origin, extent and owning asset. Contact sheets and labelled presentations belong in `preview/`, never in runtime output.

## Family-specific review checks

Check:
- declared sheet dimensions match rows, columns, cells, margins and spacing;
- every expected cell or region is represented exactly once;
- no undeclared duplicate or missing asset exists;
- edges intended to tile actually match;
- transparent areas are intentional;
- anchors and footprints are present in the manifest;
- incompatible geometries are separated.

Formal status assignment and report structure belong to file 04. Measured assembly belongs to file 11.
