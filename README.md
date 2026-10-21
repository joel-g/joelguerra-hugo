# joelguerra.com

Personal blog built with Hugo. Software engineering tutorials and Honda build guides.

## Development

Use Hugo **0.142.0 extended**, pinned in `.hugo-version`, and Python 3 (verified with 3.11). Node/npm is not needed for the site build.

```bash
# Download the checksum-verified portable Hugo binary into .tools (no PATH change)
python scripts/install_hugo.py

# Validate in staging, then replace public/ only on success
python scripts/build.py

# Build a non-indexable preview
python scripts/build.py --environment preview --destination .build/preview

# Run permanent regression checks
python -m unittest discover -s tests -v
```

For Windows authoring, run `.\.tools\hugo-0.142.0\hugo.exe server --buildDrafts --environment development`; on Linux use `./.tools/hugo-0.142.0/hugo` with those arguments. The server serves `http://localhost:1313`. The installer supports Windows/Linux x64; an existing verified executable can be supplied to the build wrapper with `--hugo`.

See the [authoring/build/release runbook](docs/authoring-and-release.md) for validation, supported commands, image retention, and release limitations. Direct Hugo commands bypass the wrapper's validation and old-asset retention.

## Content

Content lives in the `content/` directory:

- `cars/` - Honda builds, turbo projects, torque specs, how-to guides
- `tech/` - Software engineering tutorials
- `about/` - Bio page

## Adding Posts

Create a new markdown file in the appropriate content directory:

```bash
hugo new content cars/my-new-post.md
```

Front matter format:

```yaml
---
title: "Post Title"
date: 2024-01-15T10:00:00-07:00
draft: true
description: "A concise description of the article."
summary: "A short text excerpt for listing cards."
tags: ["honda", "engine"]
featured_image: "/img/folder/image.jpg"
featured_image_alt: "A useful description of the featured image."
---
```

Use the pinned executable's full path if it is not on PATH. Preview the draft and set `draft: false` only when the article is ready. Production builds exclude drafts; ordinary additions in `cars/` or `tech/` do not require rewriting the existing-route fixture. A new top-level section needs its cache-path rules reviewed.

## Images

Static assets go in `static/img/`. Reference them in posts as `/img/folder/image.jpg`.

Recommended featured image size: **1200 x 900 px**

Keep normal Markdown links and original URLs. Hugo generates responsive derivatives for supported local raster images, with access to originals for detail. Give informative images meaningful alt text. Keep diagrams legible and test narrow viewports; generated HTML checks alone do not prove visual quality.

## Theme

Uses a vendored [Ananke](https://github.com/gohugo-ananke/ananke) baseline with local overrides. Author future styling in readable `assets/css/maintenance.css`; Hugo appends it to the preserved baseline CSS and fingerprints the combined stylesheet. The [theme notes](themes/ananke/README.md) record provenance and licensing. The old Node/Webpack/changelog toolchain is removed; archived source CSS is not the active build input.

## Deploy

Cloudflare Pages automatically deploys production on pushes or merges to `master`. Local maintenance work belongs on a working branch; pushing or merging to `master` is a release action.

Hugo's default build output is `public/`. The public homepage generator was observed as Hugo 0.142.0 on October 21, 2026. Pages' configured version, build/output settings, preview configuration, and rollback deployment must still be verified before a maintenance release. A successful local build does not establish those host settings.

## Maintenance

The [implementation plan](docs/implementation-plan.md) defines local work ownership and release gates. The [milestone checklist](docs/maintenance-milestones.md) tracks acceptance criteria, including image delivery and CDN/browser caching. Local implementation and working-branch commits are authorized; production publication and live cache changes are separate decisions.

Current checkpoint: owner production/preview builds and ten independent regression tests passed, with source preservation verified. Independent cold-build QA was interrupted and remains incomplete; heavy builds and local inference are paused. Browser QA is blocked by the unavailable controllable browser surface, and host/cache/rollback verification remains open. See the plan's [execution record](docs/implementation-plan.md#execution-record) before resuming or preparing a release.

Maintenance and deployment documentation additions, October 21, 2026:

- Tars 🤖
