# func.py

def items_after_four(iter: list) -> int:
    """
    If the length of a list is less than or equal to four, return zero.
    Otherwise, return the length minus four.
    """
    if len(iter) <= 4:
        return 0
    else:
        return len(iter) - 4
if __name__ == "__main__":
    test_list = [1, 2, 3, 4, 5, 6, 7, 8]
    print(items_after_four(test_list))  # Output should be 4
