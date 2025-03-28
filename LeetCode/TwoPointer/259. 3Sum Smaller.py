'''

Description
Given an array of n integers nums and an integer target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.



Example 1:

Input: nums = [-2,0,1,3], target = 2
Output: 2
Explanation: Because there are two triplets which sums are less than 2:
[-2,0,1]
[-2,0,3]
Example 2:

Input: nums = [], target = 0
Output: 0
Example 3:

Input: nums = [0], target = 0
Output: 0


Constraints:

n == nums.length
0 <= n <= 3500
-100 <= nums[i] <= 100
-100 <= target <= 100

'''

from typing import List

# ✍️ Your function goes here
from typing import List  # Import List for type hinting

def threeSumSmaller(nums: List[int], target: int) -> int:

    nums.sort()
    triplet_count=0

    for idx in range(len(nums)):

        start_p=idx+1
        end_p=len(nums)-1

        while end_p>=start_p:

            total=nums[idx]+nums[start_p]+nums[end_p]

            if total<target:
                triplet_count=triplet_count+end_p-start_p
                start_p=start_p+1
            else:
                end_p=end_p-1

    return triplet_count


























    # nums.sort()  # Sort the array to enable two-pointer technique
    # triplet_count = 0  # Initialize counter for valid triplets
    #
    # # Iterate through the array, fixing one element at a time
    # for idx in range(len(nums) - 2):  # Up to len(nums)-3 since we need 3 elements total
    #
    #     start_p = idx + 1  # Start pointer just after fixed element
    #     end_p = len(nums) - 1  # End pointer at the last index
    #
    #     # Use two-pointer technique to find valid pairs
    #     while end_p > start_p:
    #
    #         curr_sum = nums[idx] + nums[start_p] + nums[end_p]  # Calculate sum of triplet
    #
    #         if curr_sum < target:
    #             # All elements between start_p and end_p will form valid triplets with nums[idx]
    #             triplet_count += end_p - start_p
    #             # variation if we wanted to return the list of triplets
    #             # for k in range(start_p + 1, end_p + 1):
    #             #     result.append([nums[idx], nums[start_p], nums[k]])
    #             start_p += 1  # Move start pointer to the right to explore more pairs
    #         else:
    #             end_p -= 1  # Move end pointer left to reduce the sum
    #
    # return triplet_count  # Return total count of valid triplets

"""
Time Complexity Analysis:
- Sorting takes O(n log n), where n is the length of nums.
- The outer loop runs O(n) times.
- The inner while loop (two-pointer) runs in total O(n) over all iterations.
- Overall Time Complexity: O(n^2)

Space Complexity Analysis:
- The sorting is done in-place and only a few variables are used.
- No extra data structures are used beyond input.
- Overall Space Complexity: O(1)
"""

# 🧪 Test cases with expected values
test_cases = [
    {"nums": [-2, 0, 1, 3], "target": 2, "expected": 2},
    {"nums": [], "target": 0, "expected": 0},
    {"nums": [0], "target": 0, "expected": 0},
    {"nums": [-2, 0, 1, 3], "target": 4, "expected": 3},
    {"nums": [-2, -1, 0, 3, 5], "target": 3, "expected": 5},
    {"nums": [1, 1, 1, 1], "target": 5, "expected": 4},
    {"nums": [-1, -1, -1, -1], "target": -2, "expected": 4},
    {"nums": [-100, -50, 50, 100], "target": 0, "expected": 2},
    {"nums": [0] * 3500, "target": 1, "expected": (3500 * 3499 * 3498) // 6},
    {"nums": [-100, -99, -98], "target": -296, "expected": 1},
]

# 🚀 Test runner
def run_tests():
    passed = 0
    total = len(test_cases)

    for idx, case in enumerate(test_cases, 1):
        nums = case["nums"]
        target = case["target"]
        expected = case["expected"]
        result = threeSumSmaller(nums, target)

        status = "✅ Passed" if result == expected else "❌ Failed"
        if len(nums) > 20:
            nums_display = f"{nums[:10]}...+{len(nums)-10} more"
        else:
            nums_display = nums

        print(f"Test Case {idx}: {status}")
        print(f"Input:    nums={nums_display}, target={target}")
        print(f"Your Output:   {result}")
        print(f"Expected:      {expected}")
        print("-" * 50)

        if result == expected:
            passed += 1

    print("\n====================")
    print(f"✅ Passed: {passed}/{total}")
    print("====================")

if __name__ == "__main__":
    run_tests()
