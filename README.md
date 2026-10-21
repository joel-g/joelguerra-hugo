# joelguerra.com

Personal blog built with Hugo. Software engineering tutorials and Honda build guides.

## Development

```bash
# Run local dev server
hugo server

# Build for production
hugo
```

Site available at http://localhost:1313

## Content

Content lives in the `content/` directory:

- `cars/` - Honda builds, turbo projects, torque specs, how-to guides
- `tech/` - Software engineering tutorials
- `about/` - Bio page

## Adding Posts

Create a new markdown file in the appropriate content directory:

```bash
hugo new cars/my-new-post.md
```

Front matter format:

```yaml
---
title: "Post Title"
date: 2024-01-15T10:00:00-07:00
draft: false
tags: ["honda", "engine"]
featured_image: "/img/folder/image.jpg"
---
```

## Images

Static assets go in `static/img/`. Reference them in posts as `/img/folder/image.jpg`.

Recommended featured image size: **1200 x 900 px**

## Theme

Uses the [Ananke](https://github.com/theNewDynamic/gohugo-theme-ananke) theme.

## Deploy

Cloudflare Pages automatically deploys production on pushes or merges to `master`. Local maintenance work belongs on a working branch; pushing or merging to `master` is a release action.

Hugo's default build output is `public/`. The public homepage generator was observed as Hugo 0.142.0 on October 21, 2026. Pages' configured version, build/output settings, preview configuration, and rollback deployment must still be verified before a maintenance release. A successful local build does not establish those host settings.

## Maintenance

The [implementation plan](docs/implementation-plan.md) defines local work ownership and release gates. The [milestone checklist](docs/maintenance-milestones.md) tracks acceptance criteria, including image delivery and CDN/browser caching. Local implementation and working-branch commits are authorized; production publication and live cache changes are separate decisions.

Maintenance and deployment documentation additions, October 21, 2026:

- Tars 🤖
