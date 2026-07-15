"""
Task 5: Searching
Contributor: Member C

Linear Search and Binary Search run on the same sorted list,
counting comparisons for each.
"""


def linear_search(arr, target):
    # Time Complexity: O(n) - may check every element in the worst case
    comparisons = 0
    for i, val in enumerate(arr):
        comparisons += 1
        if val == target:
            return i, comparisons
    return -1, comparisons


def binary_search(arr, target):
    # Time Complexity: O(log n) - halves the search range each step
    comparisons = 0
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, comparisons


if __name__ == "__main__":
    sorted_list = [2, 4, 7, 9, 12, 15, 18, 21, 25, 28,
                   33, 37, 41, 44, 48, 52, 57, 61, 65, 70]

    print("Sorted list (20 items):", sorted_list)

    target = 52

    idx_lin, cmp_lin = linear_search(sorted_list, target)
    print(f"\nLinear Search for {target}: found at index {idx_lin}, "
          f"comparisons = {cmp_lin}")

    idx_bin, cmp_bin = binary_search(sorted_list, target)
    print(f"Binary Search for {target}: found at index {idx_bin}, "
          f"comparisons = {cmp_bin}")

    # Extra example: value near the start, to show linear search's advantage there
    target2 = 4
    idx_lin2, cmp_lin2 = linear_search(sorted_list, target2)
    idx_bin2, cmp_bin2 = binary_search(sorted_list, target2)
    print(f"\nLinear Search for {target2}: found at index {idx_lin2}, "
          f"comparisons = {cmp_lin2}")
    print(f"Binary Search for {target2}: found at index {idx_bin2}, "
          f"comparisons = {cmp_bin2}")
