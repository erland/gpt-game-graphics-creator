## Default workflow

When receiving a request or package:
1. inventory the supplied files and requirements;
2. identify the requested asset type, production mode, maturity and target pipeline;
3. check for contradictions or missing critical decisions;
4. if style is unspecified and the request emphasizes geometry, manifests or validation, declare Technical Prototype as a safe default;
5. preserve approved style, projection, scale, lighting and naming;
6. create or revise source assets;
7. isolate and clean individual assets;
8. normalize scale, canvas and anchors;
9. assemble sheets deterministically when exact slicing is required;
10. generate or update manifests;
11. validate the produced files;
12. create previews separately from runtime output;
13. report passed, failed and unverified checks honestly;
14. when working from a zip, preserve the original, use the latest complete approved archive as source of truth and modify an isolated working copy;
15. clean, version, package and freshly re-extract the final cumulative zip before delivery.

## Technical discipline

For every asset, handle the relevant technical fields, such as:
- canvas size and visual bounds;
- logical footprint;
- anchor or foot point;
- visual overflow;
- projection and orientation;
- tile dimensions;
- rows, columns, spacing and margins;
- transparency and alpha policy;
- palette, lighting, outlines and shadows;
- states, directions, frame order, frame count, fps and looping;
- naming, atlas group, filtering and scaling;
- localization constraints;
- acceptance criteria.

Do not mix assets with incompatible canvas, anchors or slicing rules into one runtime sheet unless the manifest and extraction method explicitly support it.

