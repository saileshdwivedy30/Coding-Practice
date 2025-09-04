class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Approach 1: Hash Map (Optimal)
        Use a hash map to store numbers and their indices while iterating.
        - For each number:
            - Compute the difference: diff = target - num
            - If diff exists in the map, we have found the pair -> return indices.
            - Otherwise, add the current number and its index to the map.

        Time Complexity: O(n)
            -> Each lookup and insertion in the hash map is O(1) on average.
        Space Complexity: O(n)
            -> In the worst case, all numbers are stored in the hash map.

        Alternate Approaches:

        2) Brute Force Pairwise Check
           - Try every pair (i, j) and check if nums[i] + nums[j] == target.
           - Time Complexity: O(n^2), Space Complexity: O(1)

        3) Sorting + Two Pointers
           - Sort nums and use two pointers to find the pair.
           - Issue: Sorting loses the original indices, so requires extra bookkeeping.
           - Time Complexity: O(n log n), Space Complexity: O(1) if in place, O(n) if copying.
        """

        # Dictionary to map numbers to their indices
        number_to_index_map = {}

        # Iterate over the list with both index and number
        for idx, num in enumerate(nums):
            diff = target - num  # The number we need to find in the map

            # If the complement is already in the map, return the pair of indices
            if diff in number_to_index_map:
                return [idx, number_to_index_map[diff]]

            # Otherwise, store the current number and its index in the map
            number_to_index_map[num] = idx
