#!/usr/bin/env python
"""
Simple script to check line lengths in a file.
"""

import sys

def check_line_length(filename, max_length=80):
    """Check if any line in the file exceeds the maximum length."""
    with open(filename, 'r') as f:
        for i, line in enumerate(f, 1):
            # Remove trailing newline for accurate length check
            line = line.rstrip('\n')
            if len(line) > max_length:
                print(f"Line {i} exceeds {max_length} characters: {len(line)} chars")
                print(f"Content: {line}")
                print()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python check_line_length.py <filename> [max_length]")
        sys.exit(1)
    
    filename = sys.argv[1]
    max_length = int(sys.argv[2]) if len(sys.argv) > 2 else 80
    
    check_line_length(filename, max_length)