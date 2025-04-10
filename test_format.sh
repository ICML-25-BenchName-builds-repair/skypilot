#!/bin/bash
# Test script to verify formatting issues

# Run yapf on the specific file
yapf --diff sky/data/storage.py

# Check exit code
if [ $? -eq 0 ]; then
  echo "No formatting issues found."
  exit 0
else
  echo "Formatting issues found."
  exit 1
fi