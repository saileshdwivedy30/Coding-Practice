'''
Problem Statement #
Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.

Example 1:

Appointments: [[1,4], [2,5], [7,9]]
Output: false
Explanation: Since [1,4] and [2,5] overlap, a person cannot attend both of these appointments.
Example 2:

Appointments: [[6,7], [2,4], [8,12]]
Output: true
Explanation: None of the appointments overlap, therefore a person can attend all of them.
Example 3:

Appointments: [[4,5], [2,3], [3,6]]
Output: false
Explanation: Since [4,5] and [3,6] overlap, a person cannot attend both of these appointments.
'''


from typing import List

class Solution:
    def canAttendAppointments(self, intervals: List[List[int]]) -> bool:
        # Your code here
        if len(intervals)<=1:
            return True

        intervals.sort(key=lambda x: x[0])

        for i in range(1, len(intervals)):
            current_start=intervals[i][0]
            prev_end=intervals[i-1][1]
            if current_start <= prev_end:
                return False
        return True

# Example test cases
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    assert sol.canAttendAppointments([[1,4], [2,5], [7,9]]) == False, "Test Case 1 Failed"

    # Test Case 2
    assert sol.canAttendAppointments([[6,7], [2,4], [8,12]]) == True, "Test Case 2 Failed"

    # Test Case 3
    assert sol.canAttendAppointments([[4,5], [2,3], [3,6]]) == False, "Test Case 3 Failed"

    print("All test cases passed ✅")
