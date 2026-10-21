# Vendored Ananke theme: local maintenance notes

This repository keeps a customized Ananke baseline rather than automatically tracking upstream. The current upstream project is [Ananke](https://github.com/gohugo-ananke/ananke); upgrades require an explicit revision and review of site overrides. The historical theme metadata is not the local toolchain pin: use the site-root `.hugo-version` and the [runbook](../../docs/authoring-and-release.md).

## Active styling workflow

Author routine styling changes as readable CSS in `assets/css/maintenance.css` at the site root. Hugo concatenates it after `assets/css/ananke-baseline.css` and fingerprints the result through `layouts/partials/site-assets.html`. Run `python scripts/build.py` from the site root, then review affected desktop/mobile pages, focus behavior, contrast, and image detail. Do not edit generated output or invoke the removed Node/Webpack pipeline.

The baseline retains the 81,521-byte Git/public stylesheet originally served as `dist/css/app.1cb140d8ba31d5b2f1114537dd04802a.css`; SHA256 is `0a80155518b8c0582f505e93e4f2f4accaf500dc7dd5423f7f66b4d0a72e59c6`. A Windows auto-CRLF working copy previously differed in newline bytes; `.gitattributes` now makes the intended bytes explicit. The hash proves byte preservation only. No redesign is intended, but HTML assertions and the hash do not establish rendered visual or semantic equivalence.

Historical CSS under `src/css/` is retained for reference; it is not the active build input. If replacing the vendor baseline, record the source/upstream revision, preserve attribution and licenses, and perform a rendered comparison. Do not assume editing archived CSS will rebuild the active stylesheet.

## Dependencies, assets, and license

The unused theme-release `auto-changelog` package and the incompatible optional Webpack pipeline were removed after their references were inventoried. Site publishing uses Hugo-native assets, without npm installation. The legacy compiled CSS/JS files remain reachable so old URLs continue to work; new generated assets use versioned paths. Follow the runbook's previous-artifact retention rules for cached older pages.

The original [MIT license](LICENSE.md), author attribution, and CSS license notices remain. Keep those notices with any redistributed baseline. Site-level template and media overrides are maintained outside this vendor directory where possible.

- Tars 🤖
