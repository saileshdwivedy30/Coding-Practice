from typing import List  # For type hinting

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Sorts the list with 0s, 1s, and 2s in-place using the Dutch National Flag algorithm.
        """

        start_p, read = 0, 0  # start_p points to where 0 should go, read is current index
        end_p = len(nums) - 1  # end_p points to where 2 should go

        # Traverse the array only once
        while read <= end_p:  # Loop runs until read crosses end_p

            if nums[read] == 0:
                # Swap 0 to the front
                nums[read], nums[start_p] = nums[start_p], nums[read]
                read += 1
                start_p += 1

            elif nums[read] == 2:
                # Swap 2 to the end
                nums[read], nums[end_p] = nums[end_p], nums[read]
                end_p -= 1
                # Important: DO NOT increment read here
                # Because the swapped-in value from the end hasn't been checked yet
                # Unlike when nums[read] == 0, where we know the left side is already processed

            else:
                # nums[read] == 1, just move ahead
                read += 1

"""
Time Complexity Analysis:
- Each element is processed at most once
- Swaps and pointer moves are all constant time
- Total Time Complexity: O(n), where n is the number of elements in the list

Space Complexity Analysis:
- Sorting is done in-place
- No extra data structures used
- Total Space Complexity: O(1)
"""
