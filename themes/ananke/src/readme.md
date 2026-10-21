# Archived Ananke source assets

This directory is retained as historical reference. Its old Node/Webpack/PostCSS build and package manifests have been removed from the site's supported workflow; do not run the former npm or Yarn commands.

The active source files are `assets/css/ananke-baseline.css` and the readable `assets/css/maintenance.css` at the site root. Author normal styling changes in `maintenance.css`. Hugo concatenates and fingerprints those files; run `python scripts/build.py` from the site root and review the rendered result. Editing archived `src/css/` does not alter the active stylesheet.

See the [theme provenance/license notes](../README.md) and the [authoring/build/release runbook](../../../docs/authoring-and-release.md). Preserve the original theme's MIT license and relevant CSS notices. A future vendor-baseline update must identify its source revision and undergo visual review rather than silently reviving this obsolete toolchain.

- Tars 🤖
