'''

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

'''


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Dictionary to store numbers and their corresponding indices
        # Space Complexity: O(n) in the worst case (storing all elements)
        num_to_index = {}

        # Iterate through the list with both index and value
        # Time Complexity: O(n), as we traverse the list once
        for idx, num in enumerate(nums):

            # Compute the complement needed to reach the target
            # Time Complexity: O(1) for subtraction
            complement = target - num

            # Check if the complement is already in the dictionary
            # Time Complexity: O(1) for dictionary lookup on average
            if complement in num_to_index:
                # Return the indices of the complement and current number
                # Time Complexity: O(1) for returning the result
                return [num_to_index[complement], idx]

            # Store the current number's index in the dictionary
            # Time Complexity: O(1) for insertion into dictionary
            num_to_index[num] = idx


"""
Time Complexity Analysis:
- The function iterates through the list once → **O(n)**
- Dictionary operations (lookup and insertion) are **O(1)** on average
- Since each element is processed once, the overall time complexity is **O(n)**.

Space Complexity Analysis:
- The dictionary `num_to_index` stores at most n key-value pairs in the worst case → **O(n)**
- No additional data structures are used apart from the dictionary and a few integer variables
- Thus, the overall space complexity is **O(n)**.
"""
