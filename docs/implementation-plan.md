# Local maintenance implementation plan

Updated October 21, 2026. Base: `76ff70a541a49938f9fccef4ef43cf4d850530e9`. Integration branch: `maintenance/candidate-20261021`. The [milestone checklist](maintenance-milestones.md) contains the detailed acceptance criteria.

## Goal and authorized scope

Make this Hugo publication reproducible, lighter for readers, easier to maintain, and predictable when images are corrected. Preserve Markdown authoring, article slugs, existing image URLs, technical content, and diagrams. Keep Hugo; no framework rewrite or content-system migration is needed.

The user authorizes local implementation and working-branch commits. Cloudflare Pages deploys automatically on pushes or merges to `master`, as confirmed by the user. Do not push, merge to `master`, deploy, purge caches, change live Cloudflare configuration, access credentials, or change agent settings. Parent coordinates integration; all deliverables remain local until a separate release decision.

## Evidence gates

| Gate | Current evidence | Effect |
|---|---|---|
| Repository baseline | Base revision above; assessment found 40 Markdown documents, 36 articles, one draft, and four index pages | Use as comparison input; record any verified correction |
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

At plan creation: local implementation is authorized; the plan/checklist and deployment notes are documentation changes only. M0 remains partial. Implementation and QA results will be appended after owner handoffs; unchecked milestone items are not claims of failure or completion.

- Tars 🤖
