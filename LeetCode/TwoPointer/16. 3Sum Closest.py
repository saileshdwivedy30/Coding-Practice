'''

Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.



Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).


Constraints:

3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104


'''

from typing import List  # Import List for type hinting


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()  # Step 1: Sort the array to enable two-pointer approach
        # Time: O(n log n)
        # Space: O(1) for in-place sort

        closest_sum = float('inf')  # Initialize with a very large number

        # Step 2: Fix one element and use two pointers to find closest triplet sum
        for idx in range(len(nums)):  # Outer loop runs O(n) times
            start_p = idx + 1  # Left pointer
            end_p = len(nums) - 1  # Right pointer

            # Step 3: Two-pointer traversal
            while end_p > start_p:  # Inner loop
                curr_sum = nums[idx] + nums[start_p] + nums[end_p]  # Triplet sum

                if curr_sum == target:
                    return curr_sum  # Exact match found — best case

                # Step 4: Update closest_sum if current sum is closer to target
                if abs(target - closest_sum) > abs(target - curr_sum):
                    closest_sum = curr_sum

                # Step 5: Adjust pointers to move toward target
                if curr_sum > target:
                    end_p -= 1  # Need smaller sum
                else:
                    start_p += 1  # Need larger sum

        return closest_sum  # Return the sum closest to the target


"""
Time Complexity Analysis:
- Sorting: O(n log n)
- Outer loop: O(n)
- Inner loop (two-pointer traversal): O(n) per outer loop
- Total Time Complexity: O(n^2)

Space Complexity Analysis:
- Sorting is in-place: O(1)
- No extra data structures used
- Total Space Complexity: O(1)
"""
