class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Approach 1: Hash Maps (Optimal)
        Count the frequency of each character in both strings using hash maps (dictionaries).
        - If the lengths differ, return False immediately.
        - Build frequency maps for both strings.
        - Compare character counts between the two maps.
        - If all counts match, return True; otherwise, return False.

        Time Complexity: O(n)
            -> One pass to build frequency maps (O(n)), one pass to compare counts (O(n)).
        Space Complexity: O(1)
            -> Since the alphabet size is bounded (only lowercase English letters),
               space is effectively constant. In a more general case with arbitrary
               Unicode characters, it would be O(n).

        Alternate Approaches:

        2) Sorting Both Strings
           - Sort both strings and compare directly.
           - Time Complexity: O(n log n), Space Complexity: O(1) if sorted in place,
             O(n) if creating sorted copies.

        3) Counter Comparison (Python Built-in)
           - Use collections.Counter to count frequencies of both strings and compare.
           - Time Complexity: O(n), Space Complexity: O(1) (bounded by alphabet size).
           - Most concise in Python but less explicit than manual hash maps.

        4) Brute Force Character Removal
           - For each character in s, check if it exists in t, and remove it from t if found.
           - If all characters are matched and t is empty, return True; otherwise, False.
           - Time Complexity: O(n^2) due to repeated searches/removals in t.
           - Space Complexity: O(1).
        """

        s_map = {}
        t_map = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            s_map[s[i]] = s_map.get(s[i], 0) + 1
            t_map[t[i]] = t_map.get(t[i], 0) + 1

        for c in s_map:
            if s_map[c] != t_map.get(c, 0):
                return False
        return True
