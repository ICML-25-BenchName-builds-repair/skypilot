#!/bin/bash
# Script to verify the fix for the formatting issue

# Run yapf on the specific file that had the issue
yapf --diff ./sky/data/storage.py

# If the above command returns with exit code 0, the fix is successful
if [ $? -eq 0 ]; then
  echo "Fix successful: No formatting issues found in sky/data/storage.py"
  exit 0
else
  echo "Fix failed: Formatting issues still exist in sky/data/storage.py"
  exit 1
fi