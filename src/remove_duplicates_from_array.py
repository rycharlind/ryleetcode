# Given an integer array nums sorted in non-decreasing order, 
# remove the duplicates in-place such that each unique element appears only once. 
# The relative order of the elements should be kept the same. 
# Then return the number of unique elements in nums.


def remove_duplicates(nums):
    if not nums:
        return 0
    
    # Pointer for the position of the last unique element
    unique_pos = 0
    
    # Iterate through the array starting from the second element
    for i in range(1, len(nums)):
        # If the current element is different from the last unique element
        if nums[i] != nums[unique_pos]:
            # Move the unique element to the next position
            unique_pos += 1
            nums[unique_pos] = nums[i]
    
    # Return the number of unique elements
    return unique_pos + 1


# The reason nums still shows as [1, 1, 2] after calling remove_duplicates(nums) is that the function modifies 
# the array in place but does not remove the extra elements beyond the unique ones. 
# The function returns the count of unique elements, and you should 
# use this count to slice the array to get the unique elements.

def test_remove_duplicates():
    nums = [1, 1, 2]
    num_of_items = remove_duplicates(nums)
    assert num_of_items == 2
    assert nums[:num_of_items] == [1, 2] # When you use nums[:2], you are creating a new list that contains the elements from the start of nums up to, but not including, the element at index 2.