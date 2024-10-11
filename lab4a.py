#!/usr/bin/env python3

# Function to join two sets
def join_sets(s1, s2):
    return s1 | s2  # Returns the union of two sets

# Function to match two sets
def match_sets(s1, s2):
    return s1 & s2  # Returns the intersection of two sets

# Function to find different elements between two sets
def diff_sets(s1, s2):
    return s1 ^ s2  # Returns the symmetric difference of two sets

# Create two tuples
t1 = ('Prime', 'Ix', 'Secundus', 'Caladan')
t2 = (1, 2, 3, 4, 5, 6)

# Print elements from tuples
print(t1[0])        # Should print 'Prime'
print(t2[2:4])     # Should print (3, 4)

# Check for existence in tuple
print('Ix' in t1)   # Should print True
print('Geidi' in t1) # Should print False

# Demonstrate tuple immutability
try:
    t2[1] = 10
except TypeError as e:
    print(e)  # Should print a TypeError message

# Sets demonstration
s1 = {'Prime', 'Ix', 'Secundus', 'Caladan'}
s2 = {1, 2, 3, 4, 5}
s3 = {4, 5, 6, 7, 8}

# Attempt to access a set by index (should cause an error)
try:
    print(s1[0])
except TypeError as e:
    print(e)  # Should print a TypeError message

# Combine sets and print unique values
print(join_sets(s2, s3))  # Use the join_sets function

# Intersection of sets
print(match_sets(s2, s3))  # Use the match_sets function

# Difference
print(diff_sets(s2, s3))  # Use the diff_sets function

# Print the contents of the dictionary
dict_york = {
    'Address': '70 The Pond Rd',
    'City': 'Toronto',
    'Postal Code': 'M3J3M6',
    'Province': 'ON'
}
print(dict_york.values())  # Print all values
print(dict_york.keys())     # Print all keys

# Add and modify values
dict_york['Country'] = 'Canada'
print(dict_york)
dict_york['Province'] = 'BC'  # Change Province
print(dict_york)
