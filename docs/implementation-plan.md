# Local maintenance implementation plan

Updated October 21, 2026. Base: `76ff70a541a49938f9fccef4ef43cf4d850530e9`. Integration branch: `maintenance/candidate-20261021`. The [milestone checklist](maintenance-milestones.md) contains the detailed acceptance criteria.

## Goal and authorized scope

Make this Hugo publication reproducible, lighter for readers, easier to maintain, and predictable when images are corrected. Preserve Markdown authoring, article slugs, existing image URLs, technical content, and diagrams. Keep Hugo; no framework rewrite or content-system migration is needed.

The user authorizes local implementation and working-branch commits, and subsequently approved integrating the excerpt fix and pushing the updated candidate branch for preview. Parent coordinates that push/PR-preview cycle; Tars commits documentation locally only. Cloudflare Pages deploys production automatically on pushes or merges to `master`, as confirmed by the user. No `master` merge, production publication, purge, live Cloudflare configuration change, credential access or agent-settings change is authorized by this checkpoint.

## Evidence gates

| Gate | Current evidence | Effect |
|---|---|---|
| Repository baseline | Independent Hugo 0.142.0 baseline build: 107 pages, two paginator pages, 702 static files, three aliases; 814 output files and 76 HTML routes; zero unresolved checked local HTML asset/link targets | Compare the integrated candidate against this generated route/reference baseline |
| Content preservation | 35 published article routes match the live sitemap's 70 URLs; one draft absent from output | Keep article/image URLs and draft exclusion; the static assessment counted 36 article sources including that draft |
| Production host/trigger | User confirms Cloudflare Pages and automatic production deployment on push/merge to `master` | Treat every such operation as a release; none authorized now |
| Published Hugo generator | Public homepage reports Hugo 0.142.0; parent captured `baseline/home.html` and `baseline/home-headers.json` in the task workspace | Use 0.142.0 as the first local compatibility target; this observes the published artifact, not Pages dashboard settings |
| Production build settings | Configured Hugo version, host build command/output settings and environment remain unconfirmed | M0 stays incomplete; local version discovery and fixes may proceed |
| Preview/rollback | User-supplied hosted preview inspected; navigation and environment isolation issues remain; recoverable production deployment unconfirmed | Preview evidence is scoped; production release remains gated |
| Live caching | Prior samples: homepage DYNAMIC; article HIT with Last-Modified/304; JPG one-week freshness; SVG one-year freshness; fingerprinted CSS/JS HIT/ETag/304 | Evidence is URL-specific; raw captures, full precedence and browser correction tests remain open |

Do not mark M0 or M6 complete merely because a local build succeeds. The published generator establishes a useful compatibility target; a documented local pin does not establish the current Pages configuration. Public evidence can narrow unknowns; do not retrieve secrets or mutate account configuration to fill gaps.

## Work packages and handoffs

1. **Baseline and reproducible build — Case + Kipp; Tars records.** Case identifies/tests a concrete local Hugo version, provides deterministic build and validation commands, and inventories whether Node is needed. Kipp independently compares base/candidate routes, drafts, and representative output. Acceptance: a clean local build succeeds, validation detects deliberate failures, and the publishing commands are reproducible. No install or build script may remove the last good site assets before producing replacements.
2. **Bounded page/configuration fixes — Plex; Kipp verifies.** Fix misplaced robots configuration and preview indexing behavior; pagination canonicals/social URLs; rich listing excerpts and archive labels; social images; authoring defaults and root output ignores; heading/skip-link/contrast details. Acceptance: listed defects are corrected in generated output, page contents/URLs remain intact, and desktop/mobile navigation works. Case and Plex coordinate the shared base-template interface explicitly.
3. **Theme and dependency maintenance — Case; Tars documents decision.** Choose the smallest supported path instead of maintaining an incompatible Webpack/plugin mixture. Inventory overrides and unused release tooling; remove only confirmed-unused components or update and lock retained dependencies. Acceptance: assets are reproducibly available, retained dependency advisories have an explicit disposition, required licenses/provenance remain, and Plex's checks survive integration. Do not treat deleting a lockfile as a vulnerability fix.
4. **Media and cache policy — Case; Kipp validates.** Implement stable responsive derivatives, dimensions and appropriate loading without replacing existing original URLs. Align local header rules with mutability and avoid contradictory matches. Acceptance: deterministic reusable versioned URLs, readable diagrams, measured transfer improvement on fixed samples, and no image/reference loss. Reserve long immutable caching for truly versioned bytes; HTML and overwritten originals need a deliberate freshness/revalidation policy. Production rule precedence remains a release gate.
5. **Editorial accessibility — Plex only on an assigned article list.** Add meaningful alt descriptions and navigation headings without changing technical claims. This is optional independent work only after explicit content-path assignment; it cannot overlap Case's media edits. Acceptance: Kipp's screen-reader/keyboard/reflow samples remain understandable, with decorative images treated appropriately.
6. **Independent candidate QA — Kipp; owners repair.** Parent supplies the exact integrated candidate revision to a separate QA worktree. Kipp runs permanent checks and independent diagnostics for routes/drafts, metadata, navigation, images, a11y, responsive layout and caching. Report pass/fail/unverified by revision; do not patch application/configuration or permanent tests silently. Case/Plex own fixes and permanent test code. Tars updates the checklist and README only from verified outcomes.

## Concurrent ownership and integration

| Owner | Exclusive scope |
|---|---|
| Tars | Candidate `docs/`, `README.md`; documentation-only local commits |
| Case | Scripts, toolchain/version configuration, permanent tests, theme vendor/assets, static media/derivatives, `static/_headers`, media render hooks/partials |
| Plex | Root `config.toml`, `.gitignore`, `archetypes/`, root `layouts/` excluding Case's named media hooks/partials; article files only after explicit assignment |
| Kipp | Separate QA checkout and temporary diagnostic artifacts/report; no implementation fixes |
| Parent | Worktree coordination and candidate integration; source owners resolve overlap |

Before starting an overlapping path, agree ownership or serialize it. Case must notify Plex of required template/media interfaces; Plex must not independently invent a conflicting media API. Keep dependency/build work separate from page fixes until they can be validated together. Parent integrates scoped commits after reviewing changed paths; no broad staging, reset, stash, or automatic overwrite of another agent's work. Re-run affected checks after integration, not every unrelated check repeatedly.

Each owner hands off: branch/worktree, base/head revision, exact changed paths, commands and results, known limitations, and the next verification action. Tars's plan commit precedes major implementation. Later documentation commits record actual choices and deviations from this plan.

## Release and rollback gates

- Preserve a route/image manifest and the previous generated artifact or confirmed recoverable Pages deployment. Retain assets needed by both old and new HTML; do not prune them during rollout.
- Verify the exact Pages build/output/environment and preview settings before claiming release readiness. Ensure production indexing and preview indexing differ intentionally. Parent coordinates the approved candidate push/preview cycle; production publication remains a separate decision.
- Validate the effective live header rules separately from the checked-in `_headers` file. Test conditional requests and browser reuse independently from CDN HIT/Age. Changing a header or purging the CDN cannot expire an already-fresh browser copy.
- Rehearse a corrected image locally/in a permitted preview using a new stable versioned derivative when prompt correction requires it. Keep old original URLs; account for cached HTML; avoid random query-string cache busting. Record what the returning browser sees and when.
- Run full candidate QA and a disposable draft/new-post rehearsal. Document the rollback artifact, retained asset set, and expected browser/CDN behavior. A source revert alone is not proof of immediate visible rollback.
- Present the final local diff, candidate revision, QA evidence, remaining production unknowns, and rollback procedure. No push, `master` merge, deploy, purge, or live-rule change occurs without authorization for that release.

## Execution record

### Current checkpoint: local code `e33d28e`, hosted sample before the excerpt fix

Implementation is integrated locally on `maintenance/candidate-20261021`, code revision `e33d28ed02e9d9e2d6beb314a67f5b9ad3a96426`. It integrates Plex's `e0b6edf` excerpt fix with an identical tree, independently verified before integration. The hosted sample reviewed below predates that fix and matches sampled `797c489` production output from the prior `1e343cc` branch checkpoint. It is not evidence that the latest fix is deployed. No builds remain active; resumed local and hosted QA used no local inference. Parent owns the approved updated-branch push and hosted recheck; no background monitoring is scheduled.

| Evidence | Outcome and limit |
|---|---|
| Case implementation checks | Production/preview builds, warm builds, ten regression tests, deterministic derivative names/bytes, and deliberate broken-image failure preserving prior good output passed. These are owner checks, not final independent rendered QA. |
| Kipp independent regression tests | All 13 tests passed at `797c489`, zero skips, in 1.638 seconds, including actual generated HTML/CSS image coverage. |
| Kipp source preservation | PASS: article routes/drafts unchanged; no content files or original assets added/removed; only the starter article's 13 alt strings changed; stripping alt strings leaves its body identical. The intended `_headers` policy is the only changed original static-file Git blob. |
| Kipp independent cold build | Fresh-cache production PASS at `d8ab662` (code identical to `7ff1dbd`): Hugo 169.154 seconds, validated wrapper 173.724 seconds; 108 pages, two paginators, 702 static files, 2,032 processed images and three aliases. The earlier interrupted attempt is historical, not the current result. |
| Final correction and targeted builds | At `797c489`, warm production/preview PASS: wrapper 18.945/17.374 seconds; Hugo 9.923/12.544 seconds. The old height-auto selector failed coverage for nine home and 13 starter images; the corrected rule left zero uncovered. New CSS fingerprint emitted and prior CSS retained byte-for-byte. This is selector/markup evidence, not a rendered appearance test. |
| Output preservation and media | All 76 HTML routes, metadata and checked local references pass; no original asset loss. All 35 articles retain generated fragment IDs. All 2,029 derivatives retain their bytes after the CSS correction; independent binary dimensions and filename hashes passed on the full candidate. |
| Local authoring, retention and correction | At `d8ab662`, disposable draft exclusion/development inclusion/publication preparation passed; explicit and automatic prior-artifact retention passed; tampered retained assets failed without changing any last-good output bytes. A bounded image fixture reproduced stable URLs, produced new versions on correction, retained old versions, and restored original URLs on revert. Local artifact checks do not establish browser/CDN freshness or host rollback. |
| Excerpt follow-up | Independent `e0b6edf` production wrapper PASS in 32.814 seconds; 19 tests PASS in 2.077 seconds, zero skips. All 257 excerpts are within 220 characters with no renderer-helper leaks; five affected full-article main regions and original-image links unchanged. Old-partial negative control fails the two intended tests. All 76 HTML routes and 2,033 retained versioned media/CSS files preserved. Integrated as tree-identical `e33d28e`; hosted recheck pending. |
| Integrated excerpt candidate | Root reran production at `e33d28e`: Hugo 17.451 seconds and offline validator PASS; all 19 tests passed in 2.480 seconds, zero skips. No additional build was run by Tars for documentation. |
| Interactive QA | Earlier local browser route unavailable. Parent later passed sampled hosted desktop checks at 1180 x 757: layout, WebP/SVG/original links, skip-link focus, H1/canonical structure, code display and keyboard use. Mobile/DPR, zoom/reflow, screen-reader, measured Core Web Vitals and returning-browser cache behavior remain untested. |
| Release readiness | Not established: preview-origin navigation/environment discrepancies, configured Pages settings, host provisioning of prior artifacts, returning-browser corrected-image rollout and host rollback remain open. Sampled hosted cache directives/asset validators passed; these do not close every host gate. |

Kipp's report is task-workspace `qa-evidence/qa-report.md`. Supporting evidence includes `candidate-source-preservation.json`, `resumed-candidate-prod-build.log`, `resumed-candidate-preview-build.log`, `candidate-independent-review.json`, `article-anchor-preservation.json`, `binary-media-dimensions.json`, `remaining-integrated-checks.json`, and `authoring-and-correction-checks.json` in the same directory. The report identifies final-correction logs separately. The fresh-cache/full-scenario checks were at `d8ab662`; the later CSS/test-only change received targeted independent reruns at `797c489`. Image-size comparisons are static candidate-file budgets, not measured mobile transferred bytes or Core Web Vitals.

**Remaining QA and release steps:**

1. Parent completes the approved candidate push and rechecks the hosted excerpt fix. Coordinate scoped preview navigation/hero-origin and build-environment corrections, then verify navigation remains on preview and its HTML/robots match the intended environment while retaining HTTP noindex protection. Keep canonical/social policy separate.
2. Complete mobile/DPR, zoom/reflow, screen-reader, image-legibility/source-selection and measured transfer/performance checks. Complete fresh/returning-browser correction and revert checks; desktop screenshots and local artifact fixtures do not substitute for these.
3. Confirm actual Pages settings and a recoverable deployment, establish clean-build provisioning of all retained assets, and reconcile effective header precedence and validator behavior. Present the final revision, diff, QA results, retention mechanism and rollback target for a separate production release decision. Re-run affected checks after implementation changes; do not merge to `master`, publish production or purge automatically.

### Hosted preview evidence and open discrepancies

On October 21, 2026, Kipp read [the user-supplied preview](https://maintenance-candidate-202610.joelguerra-hugo.pages.dev/): ten URLs and 27 GET/repeat/conditional requests. Home, wiring article and page-two HTML were byte-identical to tested `797c489` production output; active CSS hash begins `c1f927`. This is sampled artifact identity, not proof of dashboard settings or the deployed Git SHA. Parent separately supplied the desktop results above.

Observed policy: HTML `public, max-age=0, must-revalidate`; mutable JPG/PNG/SVG `public, max-age=3600, must-revalidate`; hashed CSS/derivatives `public, max-age=31536000, immutable`. Seven asset/robots conditional requests returned 304 with zero body bytes. HTML exposed no ETag/Last-Modified, so its conditional behavior is untested. No Age/CF-Cache-Status was exposed; edge policy and browser reuse cannot be inferred. Captured body hashes/bytes use `Accept-Encoding: identity`, not measured mobile transfer totals.

All sampled ordinary responses carry HTTP `X-Robots-Tag: noindex`, even though HTML meta and robots are production-like. Internal navigation/brand links and hero background requests escape to production. These isolation discrepancies remain open; proposed fixes use internal relative destinations/local hero paths and the existing preview environment, subject to coordinated implementation. The excerpt helper leak found in five page-two cards is corrected locally as above, with hosted confirmation pending.

Evidence is in task-workspace `qa-evidence/hosted-preview-report.md`, `hosted-preview-responses.json`, `hosted-preview-matrix.json`, asset-identity/navigation reports and captured bodies. The excerpt checks are in `plex-excerpt-independent-report.md` and its logs/results. Its original integration-denied note is historical: explicit later approval resolved that block and parent integrated `e33d28e`.

### Implementation history

The initial plan was committed locally as `e44ee2d`. Case verified the official portable Hugo 0.142.0 extended binary's SHA256; Kipp independently built the base revision and reported the baseline checks above. Evidence is retained under `baseline/` and `qa-evidence/` in the task workspace. M0 remains partial because configured Pages settings, preview behavior, and a recoverable deployment are unverified.

The base build emits a raw-HTML warning for an existing cosmetic wrapper. Preserve that behavior and the diagram/content; do not enable unsafe HTML globally to suppress it. Parent made that scope decision after comparing the baseline.

Root made two successful bounded Offload requests to local `openai/gpt-oss-20b` with `store:false`: public manifest/config assessment (44.065 seconds command time) and cache-test planning review (50.880 seconds). These were review assistance, not implementation or QA delegation; frontier agents validated the output and rejected incorrect compatibility, redirect-cache and ordinary-image CORS claims. Token usage was not returned, so output caps are not token counts and no cost/token savings are claimed. No new inference ran during resumed/hosted QA. Exact options, provenance and rejected claims are recorded in task-workspace `qa-evidence/local-inference-usage.md`.

The checkpoint above supersedes earlier pending-status notes. Unchecked milestone items represent acceptance gates not fully closed, rather than a claim that their implementation has not begun. Local success does not clear the release gates.

Plex delivered the initial M2 changes in `c16b36a` (integrated as `e49ff10`): configuration/indexing, pagination metadata, card excerpts/navigation, authoring fields, social metadata, heading/skip-link markup. Owner checks passed with Hugo 0.142.0 and the current copied Case asset/media components, for both production and preview, plus independent `HUGO_ENV` and `HUGO_ENVIRONMENT` preview flags. Those checks were for a combined development tree, not a claim that the isolated Plex branch builds without Case's dependencies. Integrated local Kipp checks subsequently passed as recorded above; rendered QA remains open.

Plex's follow-up `230ac8b` adds 13 visually reviewed alt descriptions to the starter-replacement article, preserving technical prose, numbers, links, image URLs and order. The global source count moves from 642 to 629 empty alt occurrences out of 683; this is a bounded editorial sample, not site-wide accessibility completion. The cold media build also required the separate timeout/tooling-ignore follow-up `e7d2328`; the resumed independent fresh-cache build passed with that timeout.

Case's `e7cc58e` and `8275069` were integrated as `66d2ca4` and `7ff1dbd`: pinned portable Hugo, native CSS/media, removed unused release/obsolete bundler tooling, staged validated output, retention support, permanent checks, and disjoint provisional cache rules. The vendored CSS was preserved from the Git/public baseline, with explicit newline handling and licenses retained. No visual redesign was intended; preserved CSS bytes and HTML checks do not prove visual equivalence. Plex follow-ups were integrated as `5d7ede9` and `f2d20f4`.

Kipp's resumed review found that `.article-body img` did not match the generated image markup. Case corrected the maintained height rule and added generated-markup regression coverage in `670fa0b`, integrated as `797c489`. Kipp's negative control demonstrated the old selector gap; targeted production/preview builds and all 13 tests then passed. This closes the source finding while leaving interactive image acceptance open.

- Tars 🤖
