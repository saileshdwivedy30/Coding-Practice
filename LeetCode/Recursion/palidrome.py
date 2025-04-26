'''

Given a string s, return true if the string is palindrome, otherwise false.



A string is called palindrome if it reads the same forward and backward.


Examples:
Input : s = "hannah"

Output : true

Explanation : The string when reversed is --> "hannah", which is same as original string , so we return true.

Input : s = "aabbaaa"

Output : false

Explanation : The string when reversed is --> "aaabbaa", which is not same as original string, So we return false.

'''


class Solution:
    def palindromeCheck(self, s):
        # your code goes here

        def reverse_check(left, right):

            if left >= right:
                return True

            if s[left] != s[right]:
                return False

            return reverse_check(left + 1, right - 1)

        return reverse_check(0, len(s) - 1)