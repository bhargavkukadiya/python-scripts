# Method 1: Compare full MD5 checksums including file paths (excluding .DS_Store)
# This detects differences in both file contents and filenames/paths.
find dir1 -type f ! -name '.DS_Store' -exec md5 {} + | sort > checksums1.txt
find dir2 -type f ! -name '.DS_Store' -exec md5 {} + | sort > checksums2.txt
diff checksums1.txt checksums2.txt

# Method 2: Compare only the hash values (excluding .DS_Store)
# This ignores file paths and checks if the content is the same across directories,
# even if files are named or placed differently.
find dir1 -type f ! -name '.DS_Store' -exec md5 {} + | awk '{print $NF}' | sort > hashes1.txt
find dir2 -type f ! -name '.DS_Store' -exec md5 {} + | awk '{print $NF}' | sort > hashes2.txt
diff hashes1.txt hashes2.txt

# Method 3: Same as Method 2, but also excludes macOS AppleDouble files (._*)
# Useful for avoiding false positives due to metadata files on macOS.
find dir1 -type f ! -name '.DS_Store' ! -name '._*' -exec md5 {} + | awk '{print $NF}' | sort > hashes1.txt
find dir2 -type f ! -name '.DS_Store' ! -name '._*' -exec md5 {} + | awk '{print $NF}' | sort > hashes2.txt
diff hashes1.txt hashes2.txt

# Method 4: Use diff to recursively compare files and structure, suppressing AppleDouble file differences
# This gives a directory-level view of changes, ignoring macOS-specific metadata files.
diff -rq dir1 dir2 | grep -v '/\._'
