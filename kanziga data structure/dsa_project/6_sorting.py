"""
Task 6: Sorting
Contributor: Member D

Bubble Sort and Insertion Sort. Bubble Sort prints the array state
after each pass to show the trace.
"""


def bubble_sort(arr):
    # Time Complexity: O(n^2) - nested loops over the array
    a = arr.copy()
    n = len(a)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        print(f"  After pass {i + 1}: {a}")
        if not swapped:
            break
    return a


def insertion_sort(arr):
    # Time Complexity: O(n^2) - each insertion may shift many elements
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


if __name__ == "__main__":
    data = [29, 10, 14, 37, 4, 50, 8]
    print("Original array:", data)

    print("\n-- Bubble Sort (with trace) --")
    bubble_result = bubble_sort(data)
    print("Bubble sorted result:", bubble_result)

    print("\n-- Insertion Sort --")
    insertion_result = insertion_sort(data)
    print("Insertion sorted result:", insertion_result)
