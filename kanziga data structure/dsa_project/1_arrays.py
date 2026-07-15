"""
Task 1: Arrays
Contributor: Member A

Student marks stored in a Python list (dynamic array).
Operations: read, update, traverse, find max, insert-with-manual-shift.
"""


def read_value(arr, index):
    # Time Complexity: O(1) - direct index access
    return arr[index]


def update_value(arr, index, value):
    # Time Complexity: O(1) - direct index assignment
    arr[index] = value


def traverse(arr):
    # Time Complexity: O(n) - visits every element once
    for i, val in enumerate(arr):
        print(f"  index {i}: {val}")


def find_max(arr):
    # Time Complexity: O(n) - must inspect every element once
    max_val = arr[0]
    for val in arr[1:]:
        if val > max_val:
            max_val = val
    return max_val


def insert_at(arr, index, value):
    """
    Manually shift every element from `index` onward one position to the
    right, then place `value` in the freed slot. No built-in insert/splice
    is used.
    """
    # Time Complexity: O(n) - worst case shifts all elements after index
    arr.append(None)                       # grow the list by one slot
    for i in range(len(arr) - 1, index, -1):
        arr[i] = arr[i - 1]                # shift element right
    arr[index] = value                     # place new value in freed slot


if __name__ == "__main__":
    marks = [78, 65, 90, 55, 82]

    print("Sample input marks:", marks)

    print("\n-- Read --")
    print("Value at index 2:", read_value(marks, 2))

    print("\n-- Update --")
    update_value(marks, 1, 70)
    print("After updating index 1 to 70:", marks)

    print("\n-- Traverse --")
    traverse(marks)

    print("\n-- Find Max --")
    print("Maximum value:", find_max(marks))

    print("\n-- Insert --")
    print("Array before insertion:", marks)
    insert_at(marks, 2, 88)  # insert 88 at index 2
    print("Array after inserting 88 at index 2:", marks)
