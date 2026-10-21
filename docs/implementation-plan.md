# Local maintenance implementation plan

Updated October 21, 2026. Base: `76ff70a541a49938f9fccef4ef43cf4d850530e9`. Integration branch: `maintenance/candidate-20261021`. The [milestone checklist](maintenance-milestones.md) contains the detailed acceptance criteria.

## Goal and authorized scope

Make this Hugo publication reproducible, lighter for readers, easier to maintain, and predictable when images are corrected. Preserve Markdown authoring, article slugs, existing image URLs, technical content, and diagrams. Keep Hugo; no framework rewrite or content-system migration is needed.

The user authorizes local implementation and working-branch commits. Cloudflare Pages deploys automatically on pushes or merges to `master`, as confirmed by the user. Do not push, merge to `master`, deploy, purge caches, change live Cloudflare configuration, access credentials, or change agent settings. Parent coordinates integration; all deliverables remain local until a separate release decision.

## Evidence gates

| Gate | Current evidence | Effect |
|---|---|---|
| Repository baseline | Independent Hugo 0.142.0 baseline build: 107 pages, two paginator pages, 702 static files, three aliases; 814 output files and 76 HTML routes; zero unresolved checked local HTML asset/link targets | Compare the integrated candidate against this generated route/reference baseline |
| Content preservation | 35 published article routes match the live sitemap's 70 URLs; one draft absent from output | Keep article/image URLs and draft exclusion; the static assessment counted 36 article sources including that draft |
| Production host/trigger | User confirms Cloudflare Pages and automatic production deployment on push/merge to `master` | Treat every such operation as a release; none authorized now |
| Published Hugo generator | Public homepage reports Hugo 0.142.0; parent captured `baseline/home.html` and `baseline/home-headers.json` in the task workspace | Use 0.142.0 as the first local compatibility target; this observes the published artifact, not Pages dashboard settings |
| Production build settings | Configured Hugo version, host build command/output settings and environment remain unconfirmed | M0 stays incomplete; local version discovery and fixes may proceed |
| Preview/rollback | Host preview behavior and recoverable known-good deployment not yet evidenced | Blocks release, not local output/preview checks |
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
- Verify the exact Pages build/output/environment and preview settings before claiming release readiness. Ensure production indexing and preview indexing differ intentionally. The current task does not activate a preview or production deployment.
- Validate the effective live header rules separately from the checked-in `_headers` file. Test conditional requests and browser reuse independently from CDN HIT/Age. Changing a header or purging the CDN cannot expire an already-fresh browser copy.
- Rehearse a corrected image locally/in a permitted preview using a new stable versioned derivative when prompt correction requires it. Keep old original URLs; account for cached HTML; avoid random query-string cache busting. Record what the returning browser sees and when.
- Run full candidate QA and a disposable draft/new-post rehearsal. Document the rollback artifact, retained asset set, and expected browser/CDN behavior. A source revert alone is not proof of immediate visible rollback.
- Present the final local diff, candidate revision, QA evidence, remaining production unknowns, and rollback procedure. No push, `master` merge, deploy, purge, or live-rule change occurs without authorization for that release.

## Execution record

### Local checkpoint: code candidate `797c489`

Implementation is integrated locally on `maintenance/candidate-20261021`, code revision `797c4893b600682391fd52a419b9cee0a1f51992`. Documentation-only changes follow that revision. Independent local QA resumed and completed serially with per-process `GOMAXPROCS=2`; no builds remain active and no local inference ran during resumed QA. No background monitoring is scheduled. No push, deployment, purge, or live configuration change occurred.

| Evidence | Outcome and limit |
|---|---|
| Case implementation checks | Production/preview builds, warm builds, ten regression tests, deterministic derivative names/bytes, and deliberate broken-image failure preserving prior good output passed. These are owner checks, not final independent rendered QA. |
| Kipp independent regression tests | All 13 tests passed at `797c489`, zero skips, in 1.638 seconds, including actual generated HTML/CSS image coverage. |
| Kipp source preservation | PASS: article routes/drafts unchanged; no content files or original assets added/removed; only the starter article's 13 alt strings changed; stripping alt strings leaves its body identical. The intended `_headers` policy is the only changed original static-file Git blob. |
| Kipp independent cold build | Fresh-cache production PASS at `d8ab662` (code identical to `7ff1dbd`): Hugo 169.154 seconds, validated wrapper 173.724 seconds; 108 pages, two paginators, 702 static files, 2,032 processed images and three aliases. The earlier interrupted attempt is historical, not the current result. |
| Final correction and targeted builds | At `797c489`, warm production/preview PASS: wrapper 18.945/17.374 seconds; Hugo 9.923/12.544 seconds. The old height-auto selector failed coverage for nine home and 13 starter images; the corrected rule left zero uncovered. New CSS fingerprint emitted and prior CSS retained byte-for-byte. This is selector/markup evidence, not a rendered appearance test. |
| Output preservation and media | All 76 HTML routes, metadata and checked local references pass; no original asset loss. All 35 articles retain generated fragment IDs. All 2,029 derivatives retain their bytes after the CSS correction; independent binary dimensions and filename hashes passed on the full candidate. |
| Local authoring, retention and correction | At `d8ab662`, disposable draft exclusion/development inclusion/publication preparation passed; explicit and automatic prior-artifact retention passed; tampered retained assets failed without changing any last-good output bytes. A bounded image fixture reproduced stable URLs, produced new versions on correction, retained old versions, and restored original URLs on revert. Local artifact checks do not establish browser/CDN freshness or host rollback. |
| Interactive QA | Environment-blocked: computer-use inventory exposed no apps/browsers; the in-app route failed with `Browser is not available: iab` despite Chrome/Edge being installed. Desktop/mobile rendering, focus/keyboard, zoom, assistive technology, actual source selection and browser-cache reuse remain untested. No alternative automation or public server workaround was used. |
| Release readiness | Not established: configured Pages build/preview settings, effective deployed candidate headers, host provisioning of prior artifacts, returning-browser corrected-image rollout, and host rollback remain unverified. |

Kipp's report is task-workspace `qa-evidence/qa-report.md`. Supporting evidence includes `candidate-source-preservation.json`, `resumed-candidate-prod-build.log`, `resumed-candidate-preview-build.log`, `candidate-independent-review.json`, `article-anchor-preservation.json`, `binary-media-dimensions.json`, `remaining-integrated-checks.json`, and `authoring-and-correction-checks.json` in the same directory. The report identifies final-correction logs separately. The fresh-cache/full-scenario checks were at `d8ab662`; the later CSS/test-only change received targeted independent reruns at `797c489`. Image-size comparisons are static candidate-file budgets, not measured mobile transferred bytes or Core Web Vitals.

**Remaining QA and release steps:**

1. Restore an authorized controllable browser/assistive-technology route, then verify representative desktop/mobile pages, readable diagrams, focus/skip link, zoom/reflow, image source selection and measured network behavior. Confirm the repaired image aspect ratio in rendered output. The currently unavailable browser surface must be resolved; do not expose a local server publicly or change network settings.
2. Confirm actual Pages settings and a recoverable deployment, establish clean-build provisioning of all retained versioned assets, and verify deployed header precedence, validators and cache behavior in an authorized preview. Repeat the corrected-image/revert rehearsal with fresh and returning browsers to test the stated freshness objective; local artifact success cannot close this gate.
3. Present the final revision, diff, independent report, browser/host results, retention mechanism and rollback target for a separate release decision. Re-run affected checks if implementation changes; documentation-only commits do not establish or invalidate rendered behavior. Do not automatically push, merge to `master`, deploy or purge.

### Implementation history

The initial plan was committed locally as `e44ee2d`. Case verified the official portable Hugo 0.142.0 extended binary's SHA256; Kipp independently built the base revision and reported the baseline checks above. Evidence is retained under `baseline/` and `qa-evidence/` in the task workspace. M0 remains partial because configured Pages settings, preview behavior, and a recoverable deployment are unverified.

The base build emits a raw-HTML warning for an existing cosmetic wrapper. Preserve that behavior and the diagram/content; do not enable unsafe HTML globally to suppress it. Parent made that scope decision after comparing the baseline.

Bounded local inference reviewed public cache-regression material using `store:false`; final decisions remain with the implementing/reviewing agents. Useful Unicode/space-path fixture and redundant-fingerprint observations were retained for consideration. Incorrect redirect-cache and ordinary-image CORS claims were rejected; these are not implementation requirements.

The checkpoint above supersedes earlier pending-status notes. Unchecked milestone items represent acceptance gates not fully closed, rather than a claim that their implementation has not begun. Local success does not clear the release gates.

Plex delivered the initial M2 changes in `c16b36a` (integrated as `e49ff10`): configuration/indexing, pagination metadata, card excerpts/navigation, authoring fields, social metadata, heading/skip-link markup. Owner checks passed with Hugo 0.142.0 and the current copied Case asset/media components, for both production and preview, plus independent `HUGO_ENV` and `HUGO_ENVIRONMENT` preview flags. Those checks were for a combined development tree, not a claim that the isolated Plex branch builds without Case's dependencies. Integrated local Kipp checks subsequently passed as recorded above; rendered QA remains open.

Plex's follow-up `230ac8b` adds 13 visually reviewed alt descriptions to the starter-replacement article, preserving technical prose, numbers, links, image URLs and order. The global source count moves from 642 to 629 empty alt occurrences out of 683; this is a bounded editorial sample, not site-wide accessibility completion. The cold media build also required the separate timeout/tooling-ignore follow-up `e7d2328`; the resumed independent fresh-cache build passed with that timeout.

Case's `e7cc58e` and `8275069` were integrated as `66d2ca4` and `7ff1dbd`: pinned portable Hugo, native CSS/media, removed unused release/obsolete bundler tooling, staged validated output, retention support, permanent checks, and disjoint provisional cache rules. The vendored CSS was preserved from the Git/public baseline, with explicit newline handling and licenses retained. No visual redesign was intended; preserved CSS bytes and HTML checks do not prove visual equivalence. Plex follow-ups were integrated as `5d7ede9` and `f2d20f4`.

Kipp's resumed review found that `.article-body img` did not match the generated image markup. Case corrected the maintained height rule and added generated-markup regression coverage in `670fa0b`, integrated as `797c489`. Kipp's negative control demonstrated the old selector gap; targeted production/preview builds and all 13 tests then passed. This closes the source finding while leaving interactive image acceptance open.

- Tars 🤖
