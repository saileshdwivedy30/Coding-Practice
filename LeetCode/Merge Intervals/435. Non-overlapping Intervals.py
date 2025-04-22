'''

Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.



Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.


Constraints:

1 <= intervals.length <= 105
intervals[i].length == 2
-5 * 104 <= starti < endi <= 5 * 104

'''


from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        remove_interval_count = 0  # Count of intervals to remove

        # Intuition: Sort by end time so we always keep the interval that ends earliest
        # This leaves the most room for upcoming non-overlapping intervals
        # Time: O(n log n)
        intervals.sort(key=lambda x: x[1])

        prev = intervals[0]  # The first interval is always selected initially

        # Traverse remaining intervals
        # Time: O(n)
        for curr in intervals[1:]:
            # If current interval overlaps with previous one
            if curr[0] < prev[1]:
                remove_interval_count += 1  # Remove the current interval
            else:
                prev = curr  # No overlap, update previous to current

        return remove_interval_count  # Total intervals removed to avoid overlaps

"""
Time Complexity Analysis:
- Sorting: O(n log n), where n is the number of intervals
- Traversing intervals: O(n)
- Total Time Complexity: O(n log n)

Space Complexity Analysis:
- Sorting is done in-place
- Only a few variables used (prev, counter)
- Total Space Complexity: O(1)
"""
