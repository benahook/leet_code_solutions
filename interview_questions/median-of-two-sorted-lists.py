from typing import List


class Solution:
    def __init__(self):
        pass

    def solution(self, l1: List[int], l2: List[int]):

        merged_list = self.merge_lists(l1, l2)

        # if even grab the middle 2
        if len(merged_list) % 2 == 0:
            middle_1, middle_2 = merged_list[(len(merged_list)//2)-1], merged_list[len(merged_list)//2]
            res = (middle_1 + middle_2) / 2
        # if odd, grab the middle
        else:
            res = merged_list[len(merged_list) // 2]

        return res


    def binary_search(self, arr, left, right, target):

        if right >= left:
            mid = left + (right - left) // 2

            if arr[mid] == target:
                return mid

            elif arr[mid] > target:
                return self.binary_search(arr, left, mid - 1, target)

            else:
                return self.binary_search(arr, mid + 1, right, target)

        else:
            # target is not present in arr
            return -1

    def merge_lists(self, l1: List[int], l2: List[int]):

        n1 = len(l1)
        n2 = len(l2)

        res = []
        i, j = 0, 0

        while i < n1 and j < n2:
            if l1[i] < l2[j]:
                res.append(l1[i])
                i += 1
            else:
                res.append(l2[j])
                j += 1

        # combine what is left
        res = res + l1[i:] + l2[j:]

        return res


my_solution = Solution()
l1 = [1, 3]
l2 = [2, 7]
print(my_solution.solution(l1, l2))
