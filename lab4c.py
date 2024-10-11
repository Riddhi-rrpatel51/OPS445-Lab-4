#!/usr/bin/env python3

def create_dictionary(keys, values):
    """Combine two lists into a dictionary."""
    result_dict = {}
    for i in range(len(keys)):
        result_dict[keys[i]] = values[i]  # Combine keys and values into a dictionary
    return result_dict

def shared_values(dict1, dict2):
    """Return the set of values that are shared between two dictionaries."""
    return set(dict1.values()) & set(dict2.values())  # Intersection of values from both dictionaries

if __name__ == '__main__':
    dict_york = {
        'Address': '70 The Pond Rd',
        'City': 'Toronto',
        'Postal Code': 'M3J3M6',
        'Province': 'ON',
        'Country': 'Canada'
    }
    dict_newnham = {
        'Address': '1750 Finch Ave E',
        'City': 'Toronto',
        'Postal Code': 'M2J2X5',
        'Province': 'ON',
        'Country': 'Canada'
    }
    list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
    list_values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']
    
    # Create dictionary and print
    york = create_dictionary(list_keys, list_values)
    print('York:', york)

    # Find shared values and print
    common = shared_values(dict_york, dict_newnham)
    print('Shared Values:', common)
