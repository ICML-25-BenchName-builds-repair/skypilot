#!/bin/bash
# Test script to verify formatting issues

cd /lca-workspace/repos/skypilot-org__skypilot
yapf --diff sky/resources.py

if [ $? -eq 0 ]; then
  echo "✅ Formatting check passed!"
  exit 0
else
  echo "❌ Formatting check failed!"
  exit 1
fi