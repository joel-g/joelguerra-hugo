# Maintenance milestones and agent assignments

Assessment baseline: October 20, 2026; `joel-g/joelguerra-hugo`, base `76ff70a541a49938f9fccef4ef43cf4d850530e9`. Execution authorization updated October 21, 2026: the user authorizes the agents to implement these milestones and make local working-branch commits. Integration is on `maintenance/candidate-20261021`; never commit to `master`. The original untracked checklist in the primary checkout is preserved. Items stay open until evidence meets their acceptance checks; the [implementation plan](implementation-plan.md) records current execution gates.

The user confirms Cloudflare Pages automatically deploys on pushes or merges to `master`. No push, merge to `master`, deployment, production cache change/purge, credential access, live Cloudflare configuration change, or agent-settings change is authorized by this local implementation task. A local commit is not a release.

Keep Hugo, existing article/image URLs, and the Markdown posting workflow. Preserve published content and technical diagrams. Changes to automotive technical claims are outside this maintenance scope.

## Ownership and sequencing

| Agent | Responsibility | Boundary |
|---|---|---|
| Tars | Plans, decisions, publishing/runbook documentation, milestone handoffs | Documentation only; records evidence and unresolved decisions |
| Case | Build/dependency/theme modernization, media pipeline, cache-policy implementation when authorized | Owns major implementation and its permanent tests |
| Plex | Small, independently scoped presentation/configuration/authoring fixes | Owns bounded fixes and their permanent tests; no overlapping edits with Case |
| Kipp | Independent baseline, regression, accessibility, performance, and cache validation | Reports results and temporary diagnostics; does not silently patch application/configuration or permanent tests |

Execution order: establish the available **M0 baseline -> M1 and M2 -> M3 -> M4/M5 -> M6**. Missing production version, preview settings, or recoverable deployment evidence keeps M0 incomplete and blocks release; it does not block isolated local fixes, build discovery, or read-only cache measurements. M1 and M2 may proceed in parallel against the recorded base and path boundaries. M3 integrates their results because theme changes can supersede template fixes. Final cache implementation depends on the M4 asset naming/variant contract. M4 and M5 may overlap under the explicit ownership rules.

Use the parent-coordinated separate worktrees/branches based on the recorded revision. Tars owns `docs/` and README in the candidate worktree; Case and Plex implement in their assigned worktrees; Kipp validates in the QA worktree. The parent coordinates candidate integration. Record exact changed paths, inspect status before integration, and preserve unrelated work. Stage and commit only owned paths; no broad staging or uncoordinated resets/stashes.

## M0 — Establish the publication and verification baseline

Owner: **Tars**, with **Kipp** collecting evidence. Complete evidence is required before release; independent local work may proceed with unknowns recorded.

- [ ] **M0.1 - Identify the working deployment.** Record actual host/CDN, successful production Hugo version and build command, environment variables needed by the build (names only), publication trigger, output directory, and available preview mechanism. Acceptance: a reproducible recipe and named rollback artifact/revision exist; unknowns are explicit. The user confirms Cloudflare Pages and the `master` deployment trigger; the public homepage generator reports Hugo 0.142.0. Pages' configured version/command/output/preview settings remain unconfirmed. Local build validation is in progress; do not mark this item complete yet.
- [ ] **M0.2 — Freeze the preservation contract.** Capture published route inventory, article count, drafts, canonical/redirect behavior, and existing image URLs. Select representative home, `/cars/`, `/cars/page/2/`, `/tech/`, tag/about pages, a recent diagram article, a long photo walkthrough, and a code-heavy article. Acceptance: expected URLs and screenshots/metadata are recorded, including known defects, without changing content.
- [ ] **M0.3 — Record evidence and rollback locations.** Save a known-good generated artifact or identify the host's recoverable deployment; document how rollback selects it. Acceptance: restoring the prior artifact is feasible and retains assets needed by old pages. Do not perform production rollback or purge during planning.

## M1 — Make builds and checks repeatable

Owner: **Case**; documentation: **Tars**; acceptance: **Kipp**. Uses the available M0 baseline; production unknowns remain release gates.

Case owns version/toolchain files, CI/build scripts, dependency manifests/lockfiles, and permanent build checks. Tars owns README/runbook prose. These paths must stay separate from Plex's M2 templates/configuration.

- [ ] **M1.1 - Pin a verified local build.** Investigate available public build evidence and test a specific Hugo version locally; distinguish that tested candidate version from the still-unconfirmed production version. Document whether ordinary post publishing needs Node. Acceptance: a fresh checkout builds with the documented command, draft content stays unpublished, and generated routes match the preservation baseline. No version is described as production-known-good without evidence.
- [ ] **M1.2 — Add proportionate validation.** Build proposed changes and check local links/assets, canonical URLs including pagination, required metadata, and representative output. Acceptance: a deliberately broken local reference or build configuration makes the check fail; validation cannot deploy. Case implements permanent checks; Kipp independently demonstrates their behavior.
- [ ] **M1.3 — Resolve dependency ownership.** Separate unused theme release/changelog tooling from the asset build. Remove only confirmed-unused tooling, or update retained dependencies and regenerate a lockfile with a pinned package manager. Acceptance: retained resolved dependencies have an explained advisory result and no known applicable unresolved advisory without an explicit disposition. A deleted lockfile is not evidence of remediation. Handlebars 4.7.9 is insufficient for the October 2026 advisory set; recheck current advisories at implementation time.

## M2 — Apply small corrections without changing URLs

Owner: **Plex**; acceptance: **Kipp**. Uses the available M0 baseline and can parallel M1 with explicit ownership.

Plex owns `config.toml`, root `.gitignore`, `archetypes/default.md`, and root `layouts/` for these fixes, excluding image render hooks and media partials reserved to Case. Plex does not edit theme tooling, `static/_headers`, image files, or the theme vendor directory. New override filenames are recorded before work starts; coordinate any template that needs to call a Case-owned media partial.

| Checklist item | Acceptance check |
|---|---|
| [ ] **M2.1 — Correct robots/preview configuration** | TOML parses with `enableRobotsTXT` at the intended root; generated production robots/meta behavior is intentional; preview indexing settings work independently; no claim about live robots until checked |
| [ ] **M2.2 — Fix archive canonical/social URLs** | `/cars/page/2/` identifies itself in canonical and `og:url`; other paginator pages follow the same rule; article URLs and canonicals remain unchanged |
| [ ] **M2.3 — Bound card excerpts and clarify archives** | Listing cards contain concise text rather than tables/diagrams/video embeds; full articles retain those elements; mixed recent posts do not end with a misleading sole “All /tech” destination; useful dates remain readable |
| [ ] **M2.4 — Improve authoring defaults and metadata** | A newly scaffolded draft offers summary/description/tags/image fields; representative social previews have valid image URLs; the existing post creation command still works; build output is ignored at the site root |
| [ ] **M2.5 — Correct template accessibility details** | Consistent heading hierarchy, keyboard-visible skip link/focus, and adequate small-text contrast work at desktop/mobile widths; no lost navigation or clipped content |

Tars documents the authoring conventions after Kipp verifies them. No mass rewrite of article text is needed for this milestone.

## M3 — Establish a maintainable theme/asset path

Owner: **Case**; decision record: **Tars**; acceptance: **Kipp**. Depends on integrated M1 and M2.

- [ ] **M3.1 — Choose and record the supported approach.** Compare a pinned Ananke update, a documented vendored baseline, and a small Hugo-native asset path. Inventory the four existing site overrides and M2 additions. Acceptance: the choice explains maintenance cost and preserves required layout, Markdown, shortcodes, URLs, and image behavior. A framework rewrite is not part of this milestone.
- [ ] **M3.2 — Replace or repair the inconsistent asset pipeline.** Align retained bundler/plugins/loaders/CLI versions and lock dependency resolution. Build into temporary output before replacing final assets; do not execute the current delete-first production script in the source checkout. Acceptance: clean asset build succeeds, manifest references resolve, failure leaves the previous good assets available, and the normal site build uses the expected output.
- [ ] **M3.3 — Integrate with visual and route checks.** Acceptance: M0 samples and every M2 regression check pass; no missing assets, duplicate metadata, URL drift, or accidental draft publication. Record upstream theme revision and local override reasons. Case owns theme files and any necessary override integration in this milestone; Plex pauses template edits until it completes.

## M4 — Improve image delivery and instructional accessibility

Owner: **Case** for media; **Plex** for explicitly assigned article alt text/headings; acceptance: **Kipp**. Depends on M3.

- [ ] **M4.1 — Define a stable derivative contract.** Prioritize the largest photo tutorials and oversized listing images. Choose bounded dimensions/formats, fallback behavior, and deterministic versioned filenames. Acceptance: identical inputs produce reusable URLs; a content or transform change produces the appropriate new version; originals and existing public links remain available. Diagrams retain readable detail and access to a suitable original.
- [ ] **M4.2 — Implement responsive rendering.** Add appropriate `srcset`/sizes, intrinsic dimensions, and below-the-fold lazy loading while keeping the leading image eager. Acceptance: supported browsers receive appropriately sized images, diagrams remain legible, and before/after mobile request bytes and layout behavior are measured on the same samples. Set numerical performance targets from that baseline, not invented scores.
- [ ] **M4.3 — Add meaningful alt text and section navigation.** Plex owns an agreed article-file list only; Case owns render hooks, image-processing code, generated derivatives, and manifests. Acceptance: informative images are understandable in context; decorative/redundant images retain suitable empty alt; long walkthroughs gain useful headings without changed technical instructions. Kipp performs keyboard, zoom/reflow, and screen-reader spot checks. If Case must modify article files, serialize those files rather than sharing ownership.

## M5 — Verify and optimize CDN/browser caching

Owner: **Case** for policy and local implementation; **Kipp** for independent measurements; **Tars** for the matrix/runbook. Evidence collection can begin at M0. Local policy candidates use M4's naming contract and available evidence; effectiveness on the real host and production activation remain release gates. No live cache setting or purge is part of this task.

Parent measurements on October 20, 2026 provide an initial baseline; retain raw URLs, timestamps, request headers, and response captures with the QA evidence:

| Sample | Observed behavior | Remaining question |
|---|---|---|
| `/` | `public, max-age=604800`; `CF-Cache-Status: DYNAMIC`; no validators observed | Verify browser correction freshness and actual host rules; do not generalize to all HTML |
| `/cars/coil-on-plug-wiring-diagram/` | One-week Cache-Control; edge HIT; Last-Modified; `If-Modified-Since` returned 304 | Explain difference from homepage edge behavior and test other HTML/archive pages |
| `/img/coil-on-plug-wiring-diagram/featured.jpg` | Same one-week Cache-Control; edge HIT, ETag/increasing Age; conditional request returned 304/zero bytes; 4,991 × 3,118 pixels, 2,010,347 bytes | Resolve difference from source `/img/*` one-year rule; resizing offers substantial savings beyond TTL changes |
| `/img/coil-on-plug-wiring-diagram/wiring-diagram.svg` | `max-age=31536000` (one year) | Check correction strategy and validation; mutable `/img/` resources do not share one effective TTL |
| Fingerprinted CSS/JS | Same one-week Cache-Control; edge HIT/increasing Age; ETag conditional responses returned 304/zero bytes; no immutable observed | Confirm versioned URLs never change bytes and inspect host/header precedence |

These Cloudflare response signals do not prove which product hosts the site or reveal its complete configuration. Additional PNG/SVG coverage, future derivatives, browser reuse, and correction rollout still require validation. Exact CSS/JS sample URLs and raw captures remain to be attached under M5.1; tracked bundle filenames are not a substitute for that evidence.

- [ ] **M5.1 — Complete actual-public-behavior evidence.** Extend the initial captures to home/article/paginated HTML, mutable JPEG/PNG/SVG, fingerprinted CSS/JS, and later derivatives. Record timestamp, URL, status, `Cache-Control`, `ETag`, `Last-Modified`, `Vary`, content type/encoding, `Age`, and CDN cache-status headers where exposed. Repeated ordinary GETs and conditional GETs supplement HEAD; disabled browser caching does not measure ordinary reuse. Acceptance: a saved matrix distinguishes missing headers from unobserved behavior and includes raw evidence.
- [ ] **M5.2 — Separate browser and edge policy.** Reconcile live responses with deployed `_headers`, zone rules, and cache state: source requests one year for `/img/*`, yet the sampled JPG returns one week while SVG returns one year. Record browser freshness/revalidation separately from edge TTL, cache key, purge, and provider overrides. A CDN HIT/`Age` does not establish browser reuse. Avoid contradictory overlapping rules: if Cloudflare Pages is confirmed, [matching header rules combine](https://developers.cloudflare.com/pages/configuration/headers/) rather than simply using the last rule. Use disjoint rules or the host's documented, tested replacement mechanism. Acceptance: effective policy and precedence are explained per URL/class; exact settings remain pending verified host behavior.
- [ ] **M5.3 — Choose policy by mutability.** HTML and overwriteable originals need a suitable bounded TTL or revalidation policy, with working validators where supported. Long `max-age` plus `immutable` is reserved for truly versioned assets whose bytes never change at that URL. Apply that rule to existing fingerprints and future image derivatives only after checking the naming contract. Keep stable reusable variant URLs; avoid random query strings, unnecessary cache-busting, or uncontrolled format/size cache-key fragmentation. Acceptance: the proposed matrix balances repeat-download savings with a documented correction freshness objective; no blanket immutable rule covers mutable `/img/*` names.
- [ ] **M5.4 — Validate conditional and warm responses.** Check unchanged resources with `If-None-Match` and, where appropriate, `If-Modified-Since`; record 304/body-free revalidation or the host's explained alternative. Confirm validators change when representations change. Inspect ordinary repeated GETs for edge/cache status and test browser reuse separately. Acceptance: response bytes/requests, freshness, and variant correctness are recorded; unsupported headers or hidden edge behavior are reported rather than guessed. See [MDN Cache-Control](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cache-Control) and [MDN ETag](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/ETag).
- [ ] **M5.5 — Rehearse a corrected-image rollout in preview.** Prime a browser with the old article/image, publish a corrected test image through the proposed process, and test both a returning and fresh client. A CDN purge cannot invalidate a still-fresh browser copy, and a new response header cannot retroactively shorten its old TTL. Where prompt correction requires it, reference a new stable versioned asset while retaining the original URL; account for cached HTML still referencing the old image. Acceptance: the stated freshness objective is met, old URLs remain reachable, no incorrect format/variant is served, and reverting HTML restores a compatible retained asset. Do not purge or modify production during this rehearsal without separate authorization.

Case alone owns `static/_headers` and any verified hosting cache configuration. During M4/M5 parallel work, M4 owns media templates/derivatives and M5 owns headers/configuration; neither edits the other's paths. Tars records the policy; Kipp owns evidence, not configuration fixes.

## M6 — Release readiness and documented handoff

Owner: **Kipp** for the independent report; **Tars** for the runbook; **Case/Plex** correct findings within their assigned paths. Depends on all preceding acceptance gates.

- [ ] **M6.1 — Verify the complete candidate.** Run clean site/asset builds, permanent checks, route comparison, representative desktop/mobile reviews, image/metadata validation, and M5 cache tests. Acceptance: evidence identifies the candidate revision and separates passed, failed, and untested checks; unresolved blocking findings prevent readiness.
- [ ] **M6.2 — Rehearse ordinary posting and rollback.** Create a disposable draft, preview it, attach images, and exercise publication preparation without deploying. Restore the previous generated artifact in preview. Acceptance: the documented authoring flow remains practical, drafts are excluded, old links work, and rollback has all referenced assets. Previously cached browser responses and new versioned URLs are included in the rollback explanation.
- [ ] **M6.3 — Obtain the release decision.** Present the reviewed diff, QA evidence, artifact/revision, expected cache effects, rollback target, and any remaining limitations. Merge/push/deployment/cache-rule changes/purges require the authorization applicable at that time; this checklist grants none. After an authorized release, Kipp verifies live URLs, headers, images, and corrected-content behavior; Tars records the result. On a blocking regression, use the agreed rollback path with appropriate authorization rather than improvising a destructive fix.

- Tars 🤖
