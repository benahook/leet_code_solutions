from typing import List

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # first check if the number is divisible by 2
        # this will catch duplicates that add evenly into target

        half = target / 2
        res = []
        for index, num in enumerate(nums):
            if num == half:
                res.append(index)

        if len(res) == 2:
            return res
        elif len(res) == 1:
            # remove the half value
            half_pos = nums.index(half)
            nums[half_pos] = -1

            # then process as normal
            for num in nums:
                if target - num in nums:
                    return [nums.index(num), nums.index(target - num)]
            return [-1, -1]
        else:
            for num in nums:
                if target - num in nums:
                    return [nums.index(num), nums.index(target - num)]


t1 = Solution()
print(t1.twoSum(nums=[2, 7, 11, 5], target=9))

t2 = Solution()
print(t2.twoSum(nums=[3, 2, 4], target=6))

t3 = Solution()
print(t3.twoSum(nums=[3, 3], target=6))
