#!/bin/bash

# Test script to verify the formatting issue in docs/source/conf.py

echo "Running yapf to check formatting issues in docs/source/conf.py"
yapf --diff --recursive ./docs/source/conf.py

if [ $? -eq 0 ]; then
  echo "✅ No formatting issues found!"
  exit 0
else
  echo "❌ Formatting issues found. Please fix them."
  exit 1
fi