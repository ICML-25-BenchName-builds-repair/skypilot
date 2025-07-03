#!/usr/bin/env python3

import subprocess
import sys

def main():
    """Test the formatting of sky/resources.py."""
    cmd = [
        'yapf', '--diff', './sky/resources.py', '--lines', '835-845'
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        print("Formatting issue detected:")
        print(result.stdout)
        return 1
    else:
        print("No formatting issues found.")
        return 0

if __name__ == "__main__":
    sys.exit(main())