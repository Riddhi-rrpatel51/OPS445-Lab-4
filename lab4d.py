#!/usr/bin/env python3

def first_five(s):
    """Return the first five characters of the string."""
    return s[:5]

def last_seven(s):
    """Return the last seven characters of the string."""
    return s[-7:]

def middle_number(num):
    """Return the second and third characters of the integer as a string."""
    return str(num)[1:3]

def first_three_last_three(s1, s2):
    """Combine the first three characters of s1 with the last three characters of s2."""
    return s1[:3] + s2[-3:]

def is_digits(sobj):
    """Check if the string contains only digits."""
    return sobj.isdigit()

if __name__ == '__main__':
    # Test strings
    str1 = 'Hello World!!'
    str2 = 'Seneca College'

    # Testing string manipulation functions
    print(first_five(str1))               # Expected: 'Hello'
    print(last_seven(str1))               # Expected: 'World!!'
    print(middle_number(1500))            # Expected: '50'
    print(first_three_last_three(str1, str2))  # Expected: 'Helge'

    # Test is_digits function
    test_list = ['x3058', '3058', '8503x', '8503']
    for item in test_list:
        if is_digits(item):
            print(item, 'is an integer.')
        else:
            print(item, 'is not an integer.')
