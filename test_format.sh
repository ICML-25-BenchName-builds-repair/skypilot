#!/bin/bash
# Test script to verify the formatting issue

# Check the formatting of the file
yapf --diff sky/data/storage.py

# Exit with the same code as yapf
exit $?
