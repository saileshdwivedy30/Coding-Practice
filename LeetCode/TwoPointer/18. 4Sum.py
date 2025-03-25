'''

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.



Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]


Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109

'''

from typing import List  # For type hinting


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()  # Sort the array for duplicate handling and two-pointer logic
        # Time: O(n log n)
        # Space: O(1) if sorting is in-place

        result = []  # List to store all unique quadruplets
        # Space: O(n^2) worst case if many valid quadruplets

        # First pointer (i)
        for i in range(len(nums) - 3):  # O(n) outer loop

            # Skip duplicates for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Second pointer (j)
            for j in range(i + 1, len(nums) - 2):  # O(n) inner loop nested in i

                # Skip duplicates for j
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # Two pointers to find remaining two values
                start_p = j + 1
                end_p = len(nums) - 1

                while end_p > start_p:  # Two-pointer traversal, O(n) in total per i,j

                    total = nums[i] + nums[j] + nums[start_p] + nums[end_p]

                    if total == target:
                        # Found a valid quadruplet
                        result.append([nums[i], nums[j], nums[start_p], nums[end_p]])

                        # Skip duplicates for start_p
                        while end_p > start_p and nums[start_p] == nums[start_p + 1]:
                            start_p += 1

                        # Skip duplicates for end_p
                        while end_p > start_p and nums[end_p] == nums[end_p - 1]:
                            end_p -= 1

                        # Move both pointers after processing
                        start_p += 1
                        end_p -= 1

                    elif total > target:
                        end_p -= 1  # Need a smaller sum

                    else:
                        start_p += 1  # Need a larger sum

        return result  # Return the list of unique quadruplets


"""
Time Complexity Analysis:
- Sorting: O(n log n)
- First loop (i): O(n)
- Second loop (j): O(n)
- Two-pointer search: O(n) per i,j pair
- Total Time Complexity: O(n^3)

Space Complexity Analysis:
- Sorting is in-place: O(1)
- Result list can grow to O(n^2) in worst case
- Auxiliary space (pointers/vars): O(1)
- Total Space Complexity: O(n^2) for output, O(1) auxiliary
"""
