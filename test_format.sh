#!/bin/bash
# Test script to verify formatting issues

cd /lca-workspace/repos/skypilot-org__skypilot
yapf --diff --recursive ./sky/resources.py