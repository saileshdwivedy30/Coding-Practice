'''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]


Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
'''



class Solution:

    def sortedSquares(self, nums: List[int]) -> List[int]:

        # Initialize two pointers
        start_p = 0  # Points to the start of the array
        end_p = len(nums) - 1  # Points to the end of the array
        pos = len(nums) - 1  # Position to place the largest squared value in result
        result = [0] * len(nums)  # Create an output array of the same size

        # Process elements from both ends until the pointers meet
        while end_p >= start_p:  # Loop runs O(n) times

            # Compute squares of the elements at start and end pointers
            start_sq = nums[start_p] * nums[start_p]
            end_sq = nums[end_p] * nums[end_p]

            # Compare squared values and place the larger one at the correct position
            if end_sq >= start_sq:
                result[pos] = end_sq
                end_p -= 1  # Move the end pointer left
            else:
                result[pos] = start_sq
                start_p += 1  # Move the start pointer right

            pos -= 1  # Move the position index left

        return result  # Return the sorted squared array


"""
Time Complexity Analysis:
- The while loop runs O(n) times, where n is the length of the input list.
- Each element is processed exactly once (comparison and placement).
- Other operations (initializations, assignments, and arithmetic calculations) are O(1).
- Overall Time Complexity: O(n).

Space Complexity Analysis:
- The result list of size n takes O(n) extra space.
- Other variables (start_p, end_p, pos, start_sq, end_sq) use O(1) space.
- Overall Space Complexity: O(n).
"""
