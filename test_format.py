#!/usr/bin/env python3

import subprocess
import sys


def main():
    """Run yapf on resources.py and check if there are any formatting issues."""
    result = subprocess.run(
        ['yapf', '--diff', 'sky/resources.py'],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        print("Formatting issues found:")
        print(result.stdout)
        return 1
    else:
        print("No formatting issues found.")
        return 0


if __name__ == "__main__":
    sys.exit(main())