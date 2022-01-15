'''
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lis1=[]
        if target not in nums:
            return [-1,-1]
        else:
            for i in range(len(nums)):
                if nums[i] == target:
                    lis1.append(i)
                    break
            for i in range(len(nums)):
                nums.sort(reverse=True)
                if nums[i] == target:
                    lis1.append(len(nums)-i-1)
                    break
            return lis1
      
    
'''
Runtime: 5196 ms, faster than 5.11% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
Memory Usage: 15.5 MB, less than 55.10% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
'''        
