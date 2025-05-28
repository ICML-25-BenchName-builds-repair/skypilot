#!/usr/bin/env python3
"""
Test script to reproduce and verify the yapf formatting issue.
"""
import subprocess
import sys


def run_yapf_check():
    """Run yapf check and return the exit code."""
    cmd = [
        'yapf', '--diff', '--recursive', './', '--exclude',
        'sky/skylet/ray_patches/**', '--exclude', 'sky/skylet/providers/aws/**',
        '--exclude', 'sky/skylet/providers/gcp/**', '--exclude',
        'sky/skylet/providers/azure/**', '--exclude',
        'sky/skylet/providers/ibm/**'
    ]

    print("Running yapf formatting check...")
    print(f"Command: {' '.join(cmd)}")

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode == 0:
        print("✅ yapf formatting check PASSED")
        return True
    else:
        print("❌ yapf formatting check FAILED")
        print("STDOUT:")
        print(result.stdout)
        print("STDERR:")
        print(result.stderr)
        return False


def main():
    """Main test function."""
    print("=" * 60)
    print("Testing yapf formatting compliance")
    print("=" * 60)

    success = run_yapf_check()

    if success:
        print("\n🎉 All formatting checks passed!")
        sys.exit(0)
    else:
        print("\n💥 Formatting checks failed!")
        sys.exit(1)


if __name__ == "__main__":
    main()
