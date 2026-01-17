#!/usr/bin/env node

/**
 * Script to migrate Medium-hosted images to local static folder
 * Uses Puppeteer to bypass Cloudflare protection
 * Organizes images by blog post folder
 */

const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const CONTENT_DIR = 'content';
const IMG_BASE_DIR = 'static/img';
const DELAY_MS = 500;

async function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function downloadImage(page, url, destPath) {
    try {
        const response = await page.goto(url, { waitUntil: 'networkidle0', timeout: 30000 });

        if (!response.ok()) {
            return false;
        }

        const contentType = response.headers()['content-type'] || '';
        if (!contentType.includes('image')) {
            return false;
        }

        const buffer = await response.buffer();
        fs.writeFileSync(destPath, buffer);
        return true;
    } catch (err) {
        return false;
    }
}

async function main() {
    console.log('=== Medium Image Migration Script (Puppeteer) ===\n');

    // Find all markdown files with Medium URLs
    const grepResult = execSync(
        `grep -rlE 'cdn-images-1\\.medium\\.com|miro\\.medium\\.com' "${CONTENT_DIR}" 2>/dev/null || true`,
        { encoding: 'utf-8' }
    ).trim();

    if (!grepResult) {
        console.log('No files with Medium URLs found.');
        return;
    }

    const files = grepResult.split('\n').filter(f => f);
    console.log(`Found ${files.length} files with Medium images\n`);

    // Launch browser
    console.log('Launching browser...');
    const browser = await puppeteer.launch({
        headless: 'new',
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    });
    const page = await browser.newPage();
    await page.setUserAgent('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36');

    let totalDownloaded = 0;
    let totalFailed = 0;

    for (let fileIdx = 0; fileIdx < files.length; fileIdx++) {
        const file = files[fileIdx];
        const slug = path.basename(file, '.md');

        if (slug === '_index') continue;

        console.log(`[${fileIdx + 1}/${files.length}] Processing: ${slug}`);

        // Create image directory
        const imgDir = path.join(IMG_BASE_DIR, slug);
        if (!fs.existsSync(imgDir)) {
            fs.mkdirSync(imgDir, { recursive: true });
        }

        // Extract Medium URLs
        const content = fs.readFileSync(file, 'utf-8');
        const urlRegex = /https:\/\/(?:cdn-images-1\.medium\.com|miro\.medium\.com)\/[^)"'\s]+/g;
        const urls = [...new Set(content.match(urlRegex) || [])];

        if (urls.length === 0) {
            console.log('  No Medium URLs found');
            continue;
        }

        console.log(`  Found ${urls.length} images`);

        let downloaded = 0;
        let failed = 0;
        const mappings = [];

        for (let i = 0; i < urls.length; i++) {
            const url = urls[i];
            const origFilename = path.basename(url);

            // Determine extension
            let ext = path.extname(origFilename).slice(1) || 'jpg';
            if (ext.length > 4) ext = 'jpg'; // Handle weird extensions

            const newFilename = `${i + 1}.${ext}`;
            const destPath = path.join(imgDir, newFilename);
            const localPath = `/img/${slug}/${newFilename}`;

            // Skip if already downloaded
            if (fs.existsSync(destPath)) {
                const stats = fs.statSync(destPath);
                if (stats.size > 1000) { // More than 1KB, probably valid
                    console.log(`    [${i + 1}/${urls.length}] Exists: ${newFilename}`);
                    mappings.push({ old: url, new: localPath });
                    downloaded++;
                    continue;
                }
            }

            process.stdout.write(`    [${i + 1}/${urls.length}] Downloading: ${newFilename}... `);

            await sleep(DELAY_MS);

            if (await downloadImage(page, url, destPath)) {
                console.log('OK');
                mappings.push({ old: url, new: localPath });
                downloaded++;
            } else {
                console.log('FAILED');
                failed++;
            }
        }

        console.log(`  Downloaded: ${downloaded}, Failed: ${failed}`);

        // Update markdown file
        if (mappings.length > 0) {
            console.log('  Updating markdown file...');
            let newContent = content;
            for (const mapping of mappings) {
                newContent = newContent.split(mapping.old).join(mapping.new);
            }
            fs.writeFileSync(file, newContent);
        }

        totalDownloaded += downloaded;
        totalFailed += failed;

        // Remove empty directories
        if (fs.existsSync(imgDir) && fs.readdirSync(imgDir).length === 0) {
            fs.rmdirSync(imgDir);
        }

        console.log('');
    }

    await browser.close();

    console.log('=== Migration Complete ===');
    console.log(`Total downloaded: ${totalDownloaded}`);
    console.log(`Total failed: ${totalFailed}`);
}

main().catch(console.error);
