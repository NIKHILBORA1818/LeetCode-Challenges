'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l1=[]
        for i in range(len(nums)):
            if nums[i]+nums[i+1]==target:
                l1.append(i)
                l1.append(i+1)
                break
        return l1
