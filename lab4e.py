#!/usr/bin/env python3

def is_digits(sobj):
    """Check if the string contains only digits."""
    return sobj.isdigit()  # Returns True if the string consists of digits

if __name__ == '__main__':
    # Test cases for the is_digits function
    test_list = ['x3058', '3058', '8503x', '8503']
    for item in test_list:
        if is_digits(item):
            print(item, 'is an integer.')
        else:
            print(item, 'is not an integer.')
