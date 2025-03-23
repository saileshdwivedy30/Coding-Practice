'''

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.



Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).


Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.

'''



class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Initialize the write pointer to track the position for unique elements
        # O(1) time and O(1) space complexity
        write = 0

        # Iterate through the list starting from index 1 (since the first element is always unique)
        # The loop runs (n-1) times where n is the length of nums -> O(n) time complexity
        for read in range(1, len(nums)):

            # If the current element is different from the last unique element
            # O(1) time complexity for comparison
            if nums[read] != nums[write]:

                # Move the unique element to the next write position
                # O(1) time complexity for assignment
                nums[write + 1] = nums[read]

                # Increment the write pointer
                # O(1) time complexity
                write = write + 1

        # Return the number of unique elements (write index + 1 since it's zero-based)
        # O(1) time complexity
        return write + 1

"""
Time Complexity Analysis:
- The function uses a single loop that runs (n-1) times, where n is the length of nums.
- Each iteration includes O(1) operations (comparison and assignment).
- Therefore, the overall time complexity is O(n).

Space Complexity Analysis:
- The function modifies the input list in place and does not use extra space.
- Only a few integer variables (write, read) are used.
- Therefore, the space complexity is O(1).
"""
