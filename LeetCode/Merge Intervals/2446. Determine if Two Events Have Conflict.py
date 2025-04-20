'''

You are given two arrays of strings that represent two inclusive events that happened on the same day, event1 and event2, where:

event1 = [startTime1, endTime1] and
event2 = [startTime2, endTime2].
Event times are valid 24 hours format in the form of HH:MM.

A conflict happens when two events have some non-empty intersection (i.e., some moment is common to both events).

Return true if there is a conflict between two events. Otherwise, return false.



Example 1:

Input: event1 = ["01:15","02:00"], event2 = ["02:00","03:00"]
Output: true
Explanation: The two events intersect at time 2:00.
Example 2:

Input: event1 = ["01:00","02:00"], event2 = ["01:20","03:00"]
Output: true
Explanation: The two events intersect starting from 01:20 to 02:00.
Example 3:

Input: event1 = ["10:00","11:00"], event2 = ["14:00","15:00"]
Output: false
Explanation: The two events do not intersect.


Constraints:

event1.length == event2.length == 2
event1[i].length == event2[i].length == 5
startTime1 <= endTime1
startTime2 <= endTime2
All the event times follow the HH:MM format.

'''

from typing import List


class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        # Helper function to convert "HH:MM" time string into total minutes
        # Intuition: Converting to integers makes comparison easier
        # Time: O(1)
        def to_minutes(time_str):
            hours, mins = map(int, time_str.split(":"))  # O(1)
            return hours * 60 + mins  # O(1)

        # Convert all times to minutes for easier comparison
        # Time: O(1) per call (fixed-length strings)
        start1 = to_minutes(event1[0])
        end1 = to_minutes(event1[1])
        start2 = to_minutes(event2[0])
        end2 = to_minutes(event2[1])

        # Check for overlap between two time ranges
        # Intuition: If one event ends before the other starts, there's no conflict
        # Otherwise, there is a conflict
        # Time: O(1)
        return not (end1 < start2 or end2 < start1)


"""
Time Complexity Analysis:
- Each string is split and parsed in constant time: O(1)
- Comparison and logic: O(1)
- Total Time Complexity: O(1)

Space Complexity Analysis:
- Only integer variables used (no extra data structures)
- Total Space Complexity: O(1)
"""
from typing import List


class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        # Helper function to convert "HH:MM" time string into total minutes
        # Intuition: Converting to integers makes comparison easier
        # Time: O(1)
        def to_minutes(time_str):
            hours, mins = map(int, time_str.split(":"))  # O(1)
            return hours * 60 + mins  # O(1)

        # Convert all times to minutes for easier comparison
        # Time: O(1) per call (fixed-length strings)
        start1 = to_minutes(event1[0])
        end1 = to_minutes(event1[1])
        start2 = to_minutes(event2[0])
        end2 = to_minutes(event2[1])

        # Check for overlap between two time ranges
        # Intuition: If one event ends before the other starts, there's no conflict
        # Otherwise, there is a conflict
        # Time: O(1)
        return not (end1 < start2 or end2 < start1)


"""
Time Complexity Analysis:
- Each string is split and parsed in constant time: O(1)
- Comparison and logic: O(1)
- Total Time Complexity: O(1)

Space Complexity Analysis:
- Only integer variables used (no extra data structures)
- Total Space Complexity: O(1)
"""
