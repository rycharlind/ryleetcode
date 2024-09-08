# The time complexity of binary search is O(log n), where n is the number of elements i
# in the sorted array. This is because in each step of the algorithm, the size of the search space is halved.

# This assumes that arr is sorted.
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1 # do -1 since we start with 0

    while low <= high:
        mid = (low + high) // 2 # // = floor division
        guess = arr[mid]

        if guess == target:
            return mid
        elif guess < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def test_binary_search():
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 17
    index = binary_search(arr, target)
    assert index == 8