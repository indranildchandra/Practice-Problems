"""
Problem Statement:
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
 
Consider the number of unique elements in nums to be k. After removing duplicates, return the number of unique elements k.
 
The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.


Example 1:
nums = [1,1,2]
Output: 2
nums = [1,2,2]

Example 2:
[0,0,1,1,1,2,2,3,3,4]
Output: 5 
nums = [0,1,2,3,4,2,2,3,3,4]

"""

def remove_duplicates(nums_arr):
    pointer = 1
    for ele in nums_arr[1:]:
        # print(ele, nums_arr[pointer])
        if ele != nums_arr[pointer-1]:
            nums_arr[pointer] = ele
            pointer+=1
    # print("Output: ", pointer)
    # print("Updated Array:", nums_arr)
    return pointer, nums_arr


# Test cases
if __name__ == "__main__":
    test_cases = [
        [1, 1, 2],
        [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
        [1, 2, 3, 4, 5],
        [1, 1, 1, 1, 1],
        [1],
        [5, 5, 5, 6, 6, 7, 8, 8, 8, 9],
    ]
    
    print("=" * 60)
    print("Testing remove_duplicates function:")
    print("=" * 60)
    
    for nums in test_cases:
        print(f"\nTest Input: {nums}")
        print("-" * 60)
        original = nums.copy()
        k, updated_nums = remove_duplicates(nums)
        print(f"Result: k = {k}, \nunique elements = {nums[:k]}, \nupdated array = {updated_nums}")
        print("=" * 60)
    
    print("\nAll tests completed!")
