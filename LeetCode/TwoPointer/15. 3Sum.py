'''

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.


Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105

'''

from typing import List  # Import List for type hinting


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()  # Step 1: Sort the array
        # Time: O(n log n), where n is the length of nums
        # Space: O(1) if sorting is in-place (Python’s Timsort is in-place)

        result = []  # Initialize result list to collect valid triplets
        # Space: O(k), where k is the number of valid triplets
        # In the worst case, k can be up to O(n^2), so total space = O(n^2)

        # Step 2: Fix the first element of the triplet one by one
        for idx in range(len(nums)):  # Outer loop runs n times

            start_p = idx + 1  # Left pointer
            end_p = len(nums) - 1  # Right pointer

            # Skip duplicate fixed elements to avoid duplicate triplets
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue  # Skipping duplicates - no impact on time complexity

            # Step 3: Use two-pointer approach to find pairs that sum to -nums[idx]
            while end_p > start_p:
                # Inner loop effectively runs O(n) for each idx in total across iterations
                # So total nested complexity = O(n^2)

                total = nums[idx] + nums[start_p] + nums[end_p]

                if total == 0:
                    result.append([nums[idx], nums[start_p], nums[end_p]])  # Append triplet

                    # Skip duplicates on the left
                    while end_p > start_p and nums[start_p] == nums[start_p + 1]:
                        start_p += 1  # Skipped elements still count as part of O(n)

                    # Skip duplicates on the right
                    while end_p > start_p and nums[end_p] == nums[end_p - 1]:
                        end_p -= 1  # Also counted in total O(n)

                    # Move both pointers inward after storing the triplet
                    start_p += 1
                    end_p -= 1

                elif total > 0:
                    end_p -= 1  # Decrease sum by moving right pointer left

                else:
                    start_p += 1  # Increase sum by moving left pointer right

        return result  # Final list of all unique triplets


"""
Time Complexity Analysis:
- Sorting the array: O(n log n)
- Outer loop runs O(n) times
- Inner loop (two-pointer search) runs in total O(n) for each outer loop iteration
    => Total = O(n^2) for nested operations
- Skipping duplicates is part of pointer movement, still bounded by O(n)
- Overall Time Complexity: O(n^2)

Space Complexity Analysis:
- Auxiliary space used by the algorithm (pointers, variables): O(1)
- Output list 'result' stores up to O(k) triplets
    - In the worst case, k = O(n^2) (if all triplets are valid and unique)
- Overall Space Complexity:
    - Auxiliary: O(1)
    - Output: O(n^2) worst-case
"""
