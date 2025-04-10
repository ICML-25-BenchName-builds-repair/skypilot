#!/bin/bash
# Test script to verify formatting issues

cd "$(dirname "$0")"

# Run yapf on resources.py and check if there are any differences
yapf --diff sky/resources.py
exit_code=$?

if [ $exit_code -eq 0 ]; then
  echo "✅ No formatting issues found in sky/resources.py"
  exit 0
else
  echo "❌ Formatting issues found in sky/resources.py"
  exit 1
fi