'''
Given an array of meeting time intervals where intervals[i] = [starti, endi],
determine if a person could attend all meetings.

A person can attend all meetings if no two meetings overlap.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: False

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: True

Constraints:
0 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti < endi <= 10^6
'''

from typing import List

class Solution:
    def canAttendAppointments(self, intervals: List[List[int]]) -> bool:

        if intervals==[]:
            return True
        intervals.sort(key=lambda x: x[0])
        prev = intervals[0]

        for curr in intervals[1:]:

            if curr[0]<prev[1]:
                return False
            else:
                prev=curr
        return True

# Example test cases
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    intervals = [[0,30],[5,10],[15,20]]
    expected = False
    result = sol.canAttendAppointments(intervals)
    assert result == expected, f"Test Case 1 Failed: Expected {expected}, Got {result}"

    # Test Case 2
    intervals = [[7,10],[2,4]]
    expected = True
    result = sol.canAttendAppointments(intervals)
    assert result == expected, f"Test Case 2 Failed: Expected {expected}, Got {result}"

    # Test Case 3
    intervals = [[1,5],[5,10]]
    expected = True
    result = sol.canAttendAppointments(intervals)
    assert result == expected, f"Test Case 3 Failed: Expected {expected}, Got {result}"

    # Test Case 4
    intervals = [[1,10],[2,6],[8,12]]
    expected = False
    result = sol.canAttendAppointments(intervals)
    assert result == expected, f"Test Case 4 Failed: Expected {expected}, Got {result}"

    # Test Case 5
    intervals = []
    expected = True
    result = sol.canAttendAppointments(intervals)
    assert result == expected, f"Test Case 5 Failed: Expected {expected}, Got {result}"

    # Test Case 6
    intervals = [[5,8],[8,12],[12,15],[14,20]]
    expected = False
    result = sol.canAttendAppointments(intervals)
    assert result == expected, f"Test Case 6 Failed: Expected {expected}, Got {result}"

    print("All test cases passed ✅")
