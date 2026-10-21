# Authoring, local builds, and release gates

This runbook describes the local maintenance candidate. It does not authorize production publication. Cloudflare Pages deploys automatically when `master` is pushed or receives a merge; keep maintenance commits on the working branch until the release decision.

At code revision `797c489`, Kipp independently passed production/preview builds and all 13 regression tests with no skips, including generated-image coverage for the corrected responsive height rule. Routes, metadata, local references, original assets and derivative bytes remained intact. The preceding `d8ab662` candidate passed a fresh-cache build and local authoring, retention, failure-preservation, and image-correction rehearsals. Resumed QA is complete; no builds remain active and it used no local inference. Commands below document the supported workflow, not automatic release actions. [Revision-specific evidence and remaining release gates](implementation-plan.md#execution-record) distinguish local checks from still-unverified browser and hosting behavior.

## Toolchain and build commands

The candidate targets Hugo **0.142.0 extended**, matching the generator observed in the published homepage. Python **3.11** is the assessment environment. Node/npm is not required for the native Hugo asset path. The installer verifies pinned official archive checksums and installs a portable binary under `.tools/`; it does not change PATH or machine settings. Windows and Linux x64 archives are supported by that installer; other platforms require a separately verified matching binary.

From the repository root, when the relevant work is authorized to run:

```sh
python scripts/install_hugo.py
python scripts/build.py
python scripts/build.py --environment preview --destination .build/preview
python scripts/verify_site.py public --environment production
python scripts/verify_site.py .build/preview --environment preview
python -m unittest discover -s tests -v
```

If the verified Hugo executable already exists elsewhere, supply `--hugo ABSOLUTE_PATH_TO_HUGO` to `build.py` instead of downloading another copy. `HUGO_BINARY` also selects that executable. The script checks the pinned version and extended build, stages output, validates it, then promotes it to `public/` or the selected child of `.build/`. A failed build/check must retain the prior good output. Direct `hugo` builds do not run the wrapper's validation and retention steps.

For interactive Windows authoring with the portable installation:

```powershell
.\.tools\hugo-0.142.0\hugo.exe server --buildDrafts --environment development
```

On Linux, use `./.tools/hugo-0.142.0/hugo` with the same arguments. The server ordinarily opens at `http://localhost:1313`; it includes drafts only because this command requests them. A production build excludes drafts. Preview builds must emit `noindex, nofollow` and disallow crawling; production output must use the intended indexable behavior. Do not infer deployed preview behavior from the local environment flag alone.

## Adding and updating a post

Keep existing content filenames and slugs when correcting a published post. Create a new draft in `cars/` or `tech/` using the pinned Hugo executable, for example `hugo new content cars/my-new-post.md` if that binary is already on PATH. Otherwise invoke its full path as above.

The archetype keeps title/date and starts with `draft: true`. Its additional fields are:

| Field | Authoring purpose |
|---|---|
| `description` | A concise description for page/search/social metadata |
| `summary` | A short card excerpt; keep tables, code, diagrams, and video embeds in the article body |
| `tags` | Relevant existing tags for discovery; avoid unnecessary duplicates |
| `featured_image` | Existing-style public path such as `/img/my-new-post/cover.jpg` |
| `featured_image_alt` | Useful description for the feature image when needed by metadata/display |

Place original images in `static/img/<post>/` and continue using normal Markdown image paths. Add meaningful alt text to informative photos/diagrams; empty alt remains appropriate for decorative or fully redundant images. Preserve enough detail to read labels in wiring diagrams and other technical illustrations. The media pipeline can produce responsive versions without renaming the original public URL.

Before changing `draft` to `false`, review the article, archive card, metadata, image detail, and a narrow viewport. Run the validated production and preview builds. Existing route preservation checks must pass; additions in existing sections are allowed without editing the preserved-route fixture. A new top-level section requires an explicit cache-path policy and its validation. Never hide a removed route by deleting a baseline expectation. Do not alter unrelated automotive instructions during presentation maintenance.

The known raw-HTML warning for an existing cosmetic wrapper is preserved from the baseline. Do not enable unsafe HTML globally merely to silence it.

## Styles and image URLs

The active styles are `assets/css/ananke-baseline.css` and `assets/css/maintenance.css`, combined and fingerprinted by Hugo. The 81,521-byte baseline CSS preserves the Git/public bytes of `themes/ananke/static/dist/css/app.1cb140d8ba31d5b2f1114537dd04802a.css`; SHA256 is `0a80155518b8c0582f505e93e4f2f4accaf500dc7dd5423f7f66b4d0a72e59c6`. Narrow `.gitattributes` rules prevent platform newline conversion of legacy dist assets and enforce LF for native CSS. An earlier Windows working copy was 81,523 bytes because of newline conversion; use the Git/public digest above for provenance. Retain the theme's MIT license and provenance. Historical source CSS is archival until intentionally migrated; editing it does not update the active build.

For an existing Windows checkout, new attributes may not rewrite a previously materialized CRLF legacy stylesheet even when Git status is clean. An ordinary targeted `git restore` returned success without rewriting the candidate's stale bytes, so do not rely on that command alone. Prefer a fresh worktree/clone, or have a maintainer inspect the exact file/diff, preserve intentional edits, and refresh only that confirmed-untouched path from the committed Git blob using binary-safe I/O. Read `git show HEAD:themes/ananke/static/dist/css/app.1cb140d8ba31d5b2f1114537dd04802a.css` as bytes and write those bytes directly, without PowerShell text redirection; verify 81,521 bytes and the digest above afterward. No broad reset or restore is needed. The candidate's explicit byte-verified refresh succeeded.

For future styling changes, author readable CSS in `assets/css/maintenance.css`, the maintained layer appended after the preserved baseline. Run `python scripts/build.py` and review the affected desktop/mobile pages plus focus/contrast behavior; Hugo emits a new fingerprinted stylesheet when the combined bytes change. Do not edit generated `public/` CSS or run the removed Webpack workflow. If the vendor baseline itself needs updating, treat that as a reviewed vendor change: record the upstream revision/source, retain licenses, and compare representative rendered pages. The baseline hash proves the original bytes were preserved, not visual or semantic equivalence of the candidate. HTML assertions also cannot establish that equivalence.

Existing originals and legacy asset URLs remain available. New responsive derivatives use deterministic versioned URLs, allowing the same bytes to be cached repeatedly. Never overwrite different bytes at a versioned URL. A changed image/transform must yield a new version; avoid random per-request query strings or unnecessary duplicate variants.

Supported local raster inputs produce WebP candidates up to 640/1280 pixels at quality 82 and an original-format fallback up to 1280 pixels at quality 85, without upscaling. SVG and unsupported inputs retain their original path. Full-size article originals remain available through the generated original-image links. These choices target smaller transfers while retaining detail; actual browser source selection, transferred bytes, and visual suitability still need interactive verification.

The first full candidate generated 2,029 unique derivatives occupying 402,485,362 bytes in addition to retained originals. This is build/output storage, not bytes downloaded by each visitor. Cold processing is heavier than a cached build; the configured 300-second resource timeout replaced an insufficient 30-second default. Kipp's resumed fresh-cache production build at `d8ab662` passed in 173.724 seconds for the validated wrapper (169.154 seconds in Hugo), with per-process `GOMAXPROCS=2`. At the later CSS/test-only correction `797c489`, targeted warm production/preview builds passed in 18.945/17.374 seconds; all derivative bytes were unchanged. These are local Windows measurements, not a host build-time guarantee. `GOMAXPROCS` limits concurrent Go execution, not machine-wide CPU usage.

## Cache policy is a candidate, not a proven live result

The local `_headers` proposal separates revalidated HTML, mutable originals with a bounded one-hour freshness lifetime, and verified versioned assets with a one-year immutable lifetime. Those values are provisional policy choices, not measurements of optimal production settings. Overlapping Cloudflare Pages header matches can combine values, so the local checks reject contradictory matches.

Browser freshness and CDN edge caching are different layers. Record actual GET/conditional responses, validators, Age/cache-status headers, and browser reuse for each representative URL. Public baseline measurements differed between the homepage and an article, and between JPEG and SVG assets. A local rule-file test cannot prove what an existing Pages deployment or zone override will send.

An edge purge does not expire a fresh browser copy. Lowering today's response TTL does not change a response already stored with an older one-week/year TTL. For a correction that must appear promptly, use a new stable versioned derivative in updated HTML while retaining original URLs; also account for browsers holding older HTML. Rehearse fresh and returning clients before release.

## Retention and rollback

The validated build retains compatible versioned assets from an existing output directory. A clean checkout has no previous output to carry forward. Supply a previous complete deployment artifact explicitly when rebuilding in a clean environment:

```sh
python scripts/build.py --retain-from PATH_TO_PREVIOUS_DEPLOYMENT_ARTIFACT
```

Retain the artifact containing all assets needed by still-cacheable old HTML, including earlier retained derivatives; the immediately preceding source tree alone is insufficient. Validate hashes and reject changed bytes at existing versioned URLs. Independent local fixtures passed explicit and automatic retention, rejected a tampered retained asset without changing any prior output bytes, and preserved both versions through an image correction and revert. The final CSS correction also retained the previous fingerprinted stylesheet unchanged. The actual Pages process must still be proven to provide that artifact/retention mechanism before deploying these changes. Do not assume Pages preserves old output automatically, and do not prune retained assets during a correction rollout.

Keep a known-good deployment/artifact and the exact candidate revision. Rehearse rollback in a permitted local/preview environment, including old/new HTML references and retained media. A source revert alone does not prove that every returning browser will immediately see the previous page.

## Release checklist

- Confirm configured Pages Hugo version, build command/output, environment/preview behavior, and recoverable deployment; the observed homepage generator is not dashboard evidence.
- Obtain independent Kipp QA for the exact integrated candidate: builds, drafts, route/reference preservation, metadata, responsive rendering, a11y samples, and image/cache correction behavior. Record skipped checks honestly.
- Verify deployed header precedence and effective responses in an authorized preview. Establish artifact retention and test returning-browser correction/rollback behavior.
- Present the final diff, revision, QA results, known limitations, and rollback procedure for the release decision. No push, merge to `master`, live-rule change, purge, or production deployment is part of local validation.

Current interactive QA limitation: Kipp found Chrome/Edge installed, but the exposed computer-use inventory returned `apps: []` and `browsers: []`; the in-app browser route failed with `Browser is not available: iab`. There was no controllable browser surface through that allowed route. Rendered desktop/mobile, keyboard/focus, zoom, screen-reader, and browser-cache correction checks remain unperformed. Do not describe HTML/source checks as substitutes. No public exposure of a local server or network-settings change is permitted to work around this limitation.

- Tars 🤖
