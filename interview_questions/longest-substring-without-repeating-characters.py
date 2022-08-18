"""
Problem:
Given s, find the longest substring without repeating characters.
0 <= s.length <= 5*10^4
s contains english letters, digits, symbols, and spaces.
"""


class Solution:

    def __init__(self):
        pass

    def solution(self, s: str) -> int:
        """
        Sliding window approach to this problem
        :param s: string

        returns the integer value for the max substring length
        containing no repeating characters
        """

        # length of the input string
        n = len(s)

        # the result to return initialized at 0
        result = 0

        # outer loop n (string length) times
        for i in range(n):
            # to track all digits, lets create a "visited"
            # array that has 1 position for each ascii char (there are 256)
            # initially all positions will not be visited (False)
            # as we visit each position, we will toggle it to True
            total_ascii_chars = 256
            visited_array = [False]*total_ascii_chars

            # nested loop, i gets smaller by 1 char each iteration
            for j in range(i, n):
                # if any chars in this current window have been visited,
                # break out and slide. j is for visiting each char in the current window
                # ord() is used to return the ascii number of a given character to find it's pos
                # in the visited_array
                if visited_array[ord(s[j])] is True:
                    break
                # otherwise, we have not found a repeat
                else:
                    # use max function to measure the current window length
                    # (space between j and i), as that is the current space
                    # between non-repeating characters. assign the max to our result
                    # then continue
                    result = max(result, j - i + 1)
                    visited_array[ord(s[j])] = True

            # set visited[i] to False
            visited_array[ord(s[i])] = False

        return result


# test stub
if __name__ == "__main__":
    my_solution = Solution()
    print(my_solution.solution("abcabcbb"))
