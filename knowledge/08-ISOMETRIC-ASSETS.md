# Isometric Assets

## Purpose

Define shared projection, tile-diamond, baseline, overflow and depth-sorting rules for isometric ground, structures, props and characters.

## Projection lock

An isometric series must use one declared projection model. Record:
- logical tile width and height;
- axis directions;
- vertical-axis treatment;
- camera or projection assumption;
- orientation naming;
- world-relative lighting direction;
- scale reference.

Do not mix visually similar but mathematically incompatible angles within one runtime set.

## Tile diamond

Ground tiles intended for one grid must share an identical logical diamond and edge alignment. Texture or ornament may vary, but the underlying corners, edge paths and contact plane remain fixed.

## Foot point and anchor

Use an anchor that maps the visual object to its logical placement point. For a standing prop or character, this is normally the ground-contact point or center of the base footprint. The anchor must remain compatible across assets that share placement logic.

A tall `1x1` prop may use a larger canvas and visual overflow while retaining a `1x1` logical footprint. An object that occupies multiple cells must declare the actual footprint and reference cell.

## Visual overflow

Declare overflow above or beyond the logical footprint. Overflow must not be mistaken for occupancy. Ensure enough transparent canvas for roofs, branches, weapons, particles or cast shadows without clipping.

## Depth sorting

Provide graphics-side data that supports sorting, such as:
- foot point;
- base footprint;
- reference cell;
- visual bounds;
- optional authored sort marker when requested.

Do not claim that runtime depth sorting is verified unless tested by the developer.

## Lighting and shadows

Maintain one world-relative light direction unless the style guide explicitly permits local exceptions. Separate:
- form shading;
- contact shadow;
- cast shadow.

Cast shadows must respect the same ground plane and should not create false footprint or collision cues.

## Walls, edges and structures

For directional structures, define orientation variants and near/far visibility. Corners and junctions must align to the same projection. Multi-tile structures must specify footprint, anchor cell and overflow.

## Characters and animation

Character feet must meet the same ground plane across directions and frames. Direction changes must preserve the projection and apparent scale. File 06 owns identity/state consistency; file 07 owns temporal continuity.

## Family-specific review checks

Check:
- identical projection and tile diamond;
- consistent baseline and foot-point conventions;
- correct footprint versus overflow;
- compatible orientation variants;
- world-consistent lighting and shadows;
- sufficient canvas for height and overhang;
- graphics-side depth metadata is present;
- ground edges intended to tile align cleanly.
