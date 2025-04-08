'''

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.



Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


Constraints:

1 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 104

'''

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # Step 1: Handle edge case — null input
        # Time: O(1)
        if intervals == None:
            return intervals

        # Step 2: Sort intervals based on the start time
        # Time: O(n log n) for sorting n intervals
        intervals.sort(key=lambda x: x[0])

        # Step 3: Initialize merged list with the first interval
        # Time: O(1)
        merged = [intervals[0]]

        # Step 4: Iterate over the remaining intervals
        # Time: O(n) for iterating through the list once
        for current in intervals[1:]:
            last_merged = merged[-1]  # Time: O(1), access last element

            # Step 5: If current interval overlaps with last merged, merge them
            # Comparison: O(1)
            if current[0] <= last_merged[1]:
                # Merge: update end of the last merged interval
                # max operation is O(1)
                last_merged[1] = max(last_merged[1], current[1])
            else:
                # No overlap: add current interval as new merge
                # Append: O(1)
                merged.append(current)

        # Step 6: Return the merged list
        # Time: O(1) for return, but result list is O(n) in size
        return merged

"""
Time Complexity Analysis:
- Sorting takes O(n log n), where n is the number of intervals
- Merging loop runs O(n) in a single pass
- Total Time Complexity: O(n log n)

Space Complexity Analysis:
- Output list can hold up to O(n) intervals (in case of no merging)
- No extra data structures used beyond output
- Total Space Complexity: O(n)
"""
