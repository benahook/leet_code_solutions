"""
Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
Return the leftmost pivot index. If no such index exists, return -1.

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
"""

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_side_sum, right_side_sum = 0, 0
        i = 0
        ret_val = -1
        while i < len(nums):
            # split the arr each iteration to left/right portions each iteration
            # notice that the value at the current index is omitted.
            left_side = nums[:i]
            right_side = nums[i + 1:]

            # only sum the left and right arrays on the first iteration
            if i == 0:
                left_side_sum = 0
                right_side_sum = sum(right_side)
            else:
                # otherwise "shift" the value at our current index right to left each run
                # we accomplish this by addition and subtraction on the known starting sums
                # instead of summing the entire left and right sides each time. This drops
                # our run time complexity from a n^3 to a O(n) - constant time!
                left_side_sum += nums[i - 1]
                right_side_sum -= nums[i]

            if left_side_sum == right_side_sum:
                ret_val = i
                break

            i += 1

        return ret_val


if __name__ == '__main__':
    sol = Solution()
    print(sol.pivotIndex([1, 7, 3, 6, 5, 6]))
    print(sol.pivotIndex([1, 2, 3]))
    print(sol.pivotIndex([2, 1, -1]))
    print(sol.pivotIndex([-1, -1, -1, -1, -1, 0]))
    print(sol.pivotIndex([-1, -1, 0, 1, 0, -1]))
