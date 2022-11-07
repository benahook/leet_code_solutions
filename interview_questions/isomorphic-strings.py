"""
205. Isomorphic strings

Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.


Input: s = "egg", t = "add"
Output: true

Input: s = "foo", t = "bar"
Output: false

Input: s = "paper", t = "title"
Output: true

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.

topics:
- Hash tables

runtime:
O(n)
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        test if 2x strings are isomorphic. O(s) + O(t) + O(128ascii chars) = O(n)
        :param s:
        :param t:
        :return:
        """

        # initialize lookup hash tables containing each ascii char and empty lists
        # the list for each char will store the position that the given char appears at
        # the keys with the same length lists could potentially swap. but only if their
        # lists are equal. (the replacement letter occurs in the same place.
        s_dict = dict.fromkeys([chr(i) for i in range(128)], [])
        t_dict = dict.fromkeys([chr(i) for i in range(128)], [])

        # build the hash tables
        i = 0
        while i < len(s) and i < len(t):
            # append the current index where each char appears to the char's list in the hash table
            s_dict[s[i]] = s_dict[s[i]] + [i]
            t_dict[t[i]] = t_dict[t[i]] + [i]
            i += 1

            # then iterate s attempting transforms in hash tables
        j = 0
        while j < len(s) and j < len(t):
            if s[j] != t[j]:
                # perform lookup
                match = False
                for item in t_dict.items():
                    if item[1] == s_dict[s[j]]:
                        match = True
                if match is False:
                    return False
            j += 1

        return True
