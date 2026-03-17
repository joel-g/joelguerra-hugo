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

Build output goes to `public/`. Deploy that directory to your host.
