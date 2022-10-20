"""
Leetcode running sum of 1d integer array (list) solution
"""
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        i = 0
        output_list = [0] * len(nums)
        while i < len(nums):
            if i > 0:
                output_list[i] = nums[i] + output_list[i - 1]
            else:
                output_list[i] = nums[i]
            i += 1
        return output_list


if __name__ == '__main__':
    sol = Solution()
    print(sol.runningSum([i for i in range(1, 5)]))
    print(sol.runningSum([1] * 4))
    print(sol.runningSum([3, 1, 2, 10, 1]))
    print(sol.runningSum([1]))
    print(sol.runningSum([-1]))
    print(sol.runningSum([]))
