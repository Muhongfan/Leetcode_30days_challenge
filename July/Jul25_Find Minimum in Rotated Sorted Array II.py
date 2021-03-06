"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:

Input: [1,3,5]
Output: 1
Example 2:

Input: [2,2,2,0,1]
Output: 0
Note:

This is a follow up problem to Find Minimum in Rotated Sorted Array.
Would allow duplicates affect the run-time complexity? How and why?
"""


def findMin(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = sorted(nums)
    return nums[0]

print(findMin([1,3,5]))

#solu-less run time
def findMin2(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    start, end = 0, len(nums) - 1
    while start < end:
        mid = start + (end - start) / 2
        if nums[mid] > nums[end]:
            start = mid + 1
        elif nums[mid] < nums[end]:
            end = mid
        else:
            end -= 1
    return nums[start]