#!/bin/bash

# compare_dirs.sh
# --------------------------------------
# This script provides four different methods to compare the contents
# of two directories (dir1 and dir2), handling macOS metadata files
# like .DS_Store and AppleDouble files (._*).
#
# Usage:
#   chmod +x compare_dirs.sh
#   ./compare_dirs.sh
#
# Customize 'dir1' and 'dir2' below as needed.

# Define directories to compare
dir1="dir1"
dir2="dir2"

echo "=== Method 1: Compare full MD5 checksums including file paths ==="
find "$dir1" -type f ! -name '.DS_Store' -exec md5 {} + | sort > checksums1.txt
find "$dir2" -type f ! -name '.DS_Store' -exec md5 {} + | sort > checksums2.txt
diff checksums1.txt checksums2.txt

echo -e "\n=== Method 2: Compare only content hashes (ignoring file paths) ==="
find "$dir1" -type f ! -name '.DS_Store' -exec md5 {} + | awk '{print $NF}' | sort > hashes1.txt
find "$dir2" -type f ! -name '.DS_Store' -exec md5 {} + | awk '{print $NF}' | sort > hashes2.txt
diff hashes1.txt hashes2.txt

echo -e "\n=== Method 3: Exclude .DS_Store and AppleDouble (._*) files, compare hashes ==="
find "$dir1" -type f ! -name '.DS_Store' ! -name '._*' -exec md5 {} + | awk '{print $NF}' | sort > hashes1.txt
find "$dir2" -type f ! -name '.DS_Store' ! -name '._*' -exec md5 {} + | awk '{print $NF}' | sort > hashes2.txt
diff hashes1.txt hashes2.txt

echo -e "\n=== Method 4: Recursively compare directories and suppress AppleDouble file differences ==="
diff -rq "$dir1" "$dir2" | grep -v '/\._'
