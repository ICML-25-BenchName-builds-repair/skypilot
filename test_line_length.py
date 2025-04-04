#!/usr/bin/env python3

def check_line_length(file_path, line_number, max_length=80):
    """Check if a specific line in a file exceeds the maximum length."""
    with open(file_path, 'r') as f:
        lines = f.readlines()
        if line_number <= len(lines):
            line = lines[line_number - 1]
            line_length = len(line)
            print(f'Line {line_number} length: {line_length}')
            print(f'Line content: {line.rstrip()}')
            return line_length <= max_length
        else:
            print(f'Line {line_number} does not exist in {file_path}')
            return False

if __name__ == '__main__':
    file_path = 'sky/resources.py'
    line_number = 839
    result = check_line_length(file_path, line_number)
    print(f'Line length check passed: {result}')