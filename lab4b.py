#!/usr/bin/env python3

def join_lists(l1, l2):
    return list(set(l1) | set(l2))  # Return a list containing all unique values from both lists

def match_lists(l1, l2):
    return list(set(l1) & set(l2))  # Return a list containing common values from both lists

def diff_lists(l1, l2):
    return list(set(l1) ^ set(l2))  # Return a list containing different values between both lists

if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = [3, 4, 5]
    print('join:', join_lists(list1, list2))
    print('match:', match_lists(list1, list2))
    print('diff:', diff_lists(list1, list2))
