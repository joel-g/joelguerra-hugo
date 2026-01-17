#!/bin/bash

# Script to migrate Medium-hosted images to local static folder
# Uses Wayback Machine to bypass Cloudflare protection
# Organizes images by blog post folder

set -e

CONTENT_DIR="content"
IMG_BASE_DIR="static/img"
DELAY=1  # Delay between requests

echo "=== Medium Image Migration Script ==="
echo ""

# Find all markdown files with Medium URLs
files=$(grep -rlE 'cdn-images-1\.medium\.com|miro\.medium\.com' "$CONTENT_DIR" 2>/dev/null || true)

if [ -z "$files" ]; then
    echo "No files with Medium URLs found."
    exit 0
fi

total_files=$(echo "$files" | wc -l | tr -d ' ')
echo "Found $total_files files with Medium images"
echo ""

file_count=0
total_downloaded=0
total_failed=0

for file in $files; do
    file_count=$((file_count + 1))

    # Get the slug from the filename (without .md extension)
    slug=$(basename "$file" .md)

    # Skip _index files
    if [ "$slug" = "_index" ]; then
        continue
    fi

    echo "[$file_count/$total_files] Processing: $slug"

    # Create image directory for this post
    img_dir="$IMG_BASE_DIR/$slug"
    mkdir -p "$img_dir"

    # Extract Medium URLs from this file
    urls=$(grep -oE 'https://cdn-images-1\.medium\.com/[^)"'"'"' ]+|https://miro\.medium\.com/[^)"'"'"' ]+' "$file" | sort -u)

    if [ -z "$urls" ]; then
        echo "  No Medium URLs found (might be in frontmatter only)"
        continue
    fi

    url_count=$(echo "$urls" | wc -l | tr -d ' ')
    echo "  Found $url_count images"

    downloaded=0
    failed=0
    img_num=0

    # Create a temporary file for URL mappings
    mapping_file=$(mktemp)

    for url in $urls; do
        img_num=$((img_num + 1))

        # Get original filename and extension
        orig_filename=$(basename "$url")

        # Determine extension (some URLs don't have one)
        if [[ "$orig_filename" == *.* ]]; then
            ext="${orig_filename##*.}"
        else
            ext="jpg"  # Default to jpg if no extension
        fi

        # Create a clean numbered filename
        new_filename="${img_num}.${ext}"
        dest_path="$img_dir/$new_filename"
        local_path="/img/$slug/$new_filename"

        # Skip if already downloaded
        if [ -f "$dest_path" ] && ! file "$dest_path" | grep -q "HTML"; then
            echo "    [$img_num/$url_count] Exists: $new_filename"
            echo "$url|$local_path" >> "$mapping_file"
            downloaded=$((downloaded + 1))
            continue
        fi

        echo -n "    [$img_num/$url_count] Downloading: $new_filename... "

        sleep $DELAY

        # Try Wayback Machine first
        wayback_url="https://web.archive.org/web/2024/$url"

        if curl -sL --fail -o "$dest_path" "$wayback_url" 2>/dev/null; then
            # Verify it's an image
            if file "$dest_path" | grep -qE "image|JPEG|PNG|GIF|WebP"; then
                echo "OK (wayback)"
                echo "$url|$local_path" >> "$mapping_file"
                downloaded=$((downloaded + 1))
            else
                echo "FAILED (not an image)"
                rm -f "$dest_path"
                failed=$((failed + 1))
            fi
        else
            # Try direct download as fallback
            if curl -sL --fail \
                -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36" \
                -o "$dest_path" "$url" 2>/dev/null; then
                if file "$dest_path" | grep -qE "image|JPEG|PNG|GIF|WebP"; then
                    echo "OK (direct)"
                    echo "$url|$local_path" >> "$mapping_file"
                    downloaded=$((downloaded + 1))
                else
                    echo "FAILED (not an image)"
                    rm -f "$dest_path"
                    failed=$((failed + 1))
                fi
            else
                echo "FAILED"
                rm -f "$dest_path"
                failed=$((failed + 1))
            fi
        fi
    done

    echo "  Downloaded: $downloaded, Failed: $failed"

    # Update the markdown file with local paths
    if [ -s "$mapping_file" ]; then
        echo "  Updating markdown file..."

        temp_file=$(mktemp)
        cp "$file" "$temp_file"

        while IFS='|' read -r old_url new_path; do
            # Escape special characters for sed
            old_escaped=$(printf '%s\n' "$old_url" | sed 's/[[\.*^$()+?{|]/\\&/g')
            new_escaped=$(printf '%s\n' "$new_path" | sed 's/[&/\]/\\&/g')
            sed -i '' "s|$old_escaped|$new_escaped|g" "$temp_file"
        done < "$mapping_file"

        mv "$temp_file" "$file"
    fi

    rm -f "$mapping_file"

    total_downloaded=$((total_downloaded + downloaded))
    total_failed=$((total_failed + failed))

    # Remove empty image directories
    if [ -d "$img_dir" ] && [ -z "$(ls -A "$img_dir")" ]; then
        rmdir "$img_dir"
    fi

    echo ""
done

echo "=== Migration Complete ==="
echo "Total downloaded: $total_downloaded"
echo "Total failed: $total_failed"
