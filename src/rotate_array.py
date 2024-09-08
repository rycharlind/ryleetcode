# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

# Solution 1: Using List Slicing
# - List slicing takes O(n) time, where n is the number of elements in the array.
# - Modulus Operation: k %= len(nums) ensures that k is within the bounds of the list's length. 
#   If k is greater than the length of the list, this operation will reduce k to a 
#   value that is effectively the same as rotating the list by k % len(nums) positions. 
#   For example, rotating a list of length 5 by 7 positions is the same as rotating it by 2 positions.
def rotate1(nums, k):
    k %= len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    return nums

# Solution 2: Using Extra Array
# The loop runs n times where n is the number of elements in the array, so the time complexity is O(n).
# This solution uses O(n) extra space for the result array.
def rotate2(nums, k):
    n = len(nums)
    k %= n
    result = [0] * n
    for i in range(n):
        result[(i + k) % n] = nums[i]
    nums[:] = result
    return nums

# Solution 3: Reversing Array in Place
# Reversing the entire array takes O(n) time.
# Reversing two subarrays takes O(k) and O(n-k) time respectively.
# Overall, the time complexity is O(n).
# This solution uses O(1) extra space as it performs the rotation in place.
def rotate3(nums, k):
    def reverse(arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    n = len(nums)
    k %= n
    reverse(nums, 0, n - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, n - 1)
    
    return nums


k = 3
expected_output = [5,6,7,1,2,3,4]

def test_rotate1():
    input = [1,2,3,4,5,6,7]
    output1 = rotate1(input, k)
    print(output1)
    assert output1 == expected_output

def test_rotate2():
    input = [1,2,3,4,5,6,7]
    output2 = rotate2(input, k)
    print(output2)
    assert output2 == expected_output

def test_rotate3():
    input = [1,2,3,4,5,6,7]
    output3 = rotate3(input, k)
    print(output3)
    assert output3 == expected_output