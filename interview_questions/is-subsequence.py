"""
392. Is Subsequence.

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none)
of the characters without disturbing the relative positions of the remaining characters.
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Examples:

Input: s = "abc", t = "ahbgdc"
Output: true

Input: s = "axc", t = "ahbgdc"
Output: false

Constraints:
0 <= s.length <= 100
0 <= t.length <= 10^4
s and t consist only of lowercase English letters

I believe this is O(nlogn) since the J loop shrinks each i iteration
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # binary list to track found letters
        b_list = [False] * len(s)
        i, j = 0, 0
        # iterate each char in s
        while i < len(s):
            # scan t from each i in s
            while j < len(t):
                # if we have a match break out of j loop
                if s[i] == t[j]:
                    b_list[i] = True
                    j += 1
                    break
                else:
                    j += 1

            # if no matches are found in j loop (the char isn't found in t) return False
            if b_list[i] is False:
                return False
            # otherwise continue iterating s
            i += 1

        if all(b_list):
            return True


if __name__ == '__main__':
    my_sol = Solution()
    print(my_sol.isSubsequence("abc", "ahbgdc"))
    print(my_sol.isSubsequence("axc", "ahbgdc"))
    print(my_sol.isSubsequence("a" * 100, "b" * int(10e4)))
    print(my_sol.isSubsequence("aaaaaa", "bbbaaaa"))
    print(my_sol.isSubsequence("ab", "baab"))
