'''

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.



Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false


Constraints:

1 <= n <= 231 - 1
'''


class Solution:
    def isHappy(self, n: int) -> bool:

        # Helper function to compute the sum of squares of digits
        def get_number(number):
            total = 0
            while number > 0:
                digit = number % 10
                total += digit * digit
                number = number // 10
            return total

        # Initialize slow and fast pointers
        slow = n
        fast = get_number(n)

        # Continue until fast becomes 1 (happy number) - here the cycle is only around 1
        # or fast meets slow (cycle — not a happy number) - here the cycle is around a number which is not 1

        # So the thing is if for a number if fast reaches 1 then it is a happy number already,
        # and yes eventually slow and fast will meet. But as soon as fast reaches 1 we can safely say it a happy number
        # no need to wait for slow and fast to meet.
        while fast != 1 and fast != slow:
            slow = get_number(slow)  # move 1 step
            fast = get_number(get_number(fast))  # move 2 steps

        # If fast reaches 1, it's a happy number
        return fast == 1


"""
Time Complexity Analysis:
- Each transformation (sum of squares of digits) takes O(log n) time (due to digit count)
- In the worst case, it loops through a known small cycle of non-happy numbers
- So it's effectively bounded and converges quickly
- Total Time Complexity: O(log n)

Space Complexity Analysis:
- Only uses a few integer variables
- No additional data structures
- Total Space Complexity: O(1)
"""
