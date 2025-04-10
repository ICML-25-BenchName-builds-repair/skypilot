#!/bin/bash
# Simple script to test pylint on the resources.py file
cd /lca-workspace/repos/skypilot-org__skypilot
cat sky/resources.py | wc -L  # Check the maximum line length
echo "Line 839:"
sed -n '839p' sky/resources.py | wc -c  # Check the length of line 839
echo "Content of line 839:"
sed -n '839p' sky/resources.py