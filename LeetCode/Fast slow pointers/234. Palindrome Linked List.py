'''

Palindrome LinkedList (medium) #
Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.

Your algorithm should use constant space and the input LinkedList should be in the original form once the algorithm is finished. The algorithm should have
O
(
N
)
O(N) time complexity where ‘N’ is the number of nodes in the LinkedList.

Example 1:

Input: 2 -> 4 -> 6 -> 4 -> 2 -> null
Output: true
Example 2:

Input: 2 -> 4 -> 6 -> 4 -> 2 -> 2 -> null
Output: false

'''

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    # Helper function to reverse a linked list
    def reverse(self, head):
        curr = head
        prev = None

        while curr:
            temp_next = curr.next     # Save the next node
            curr.next = prev          # Reverse the link
            prev = curr               # Move prev to current
            curr = temp_next          # Move to next node

        return prev  # New head of the reversed list

    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # Step 1: Handle corner cases
        if head is None or head.next is None:
            return True  # Empty list or single node is always a palindrome

        # Step 2: Use two pointers to find the middle of the list
        fast = head
        slow = head

        # We check both fast and fast.next because fast moves two steps
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Step 3: Reverse the second half of the list
        second_head = self.reverse(slow)

        # Step 4: Compare first half and reversed second half
        first, second = head, second_head
        result = True
        while second:  # Only need to compare until second half ends
            if first.val != second.val:
                result = False  # Values don't match
            first = first.next
            second = second.next

        # Step 5: Restore the original list (good for interviews!)
        self.reverse(slow)

        return result  # Return whether it's a palindrome

"""
Time Complexity Analysis:
- Finding the middle: O(n)
- Reversing the second half: O(n)
- Comparing both halves: O(n)
- Restoring the list
- Total Time Complexity: O(n)

Space Complexity Analysis:
- Only uses a few pointers (slow, fast, prev, etc.)
- No additional data structures
- Total Space Complexity: O(1)
"""
