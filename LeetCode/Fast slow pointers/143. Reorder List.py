'''

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.



Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]


Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000

'''
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    # Helper function to reverse a linked list
    # Time: O(n), Space: O(1)
    def reverse(self, head):
        prev = None
        curr = head

        while curr:  # O(n)
            temp_next = curr.next       # O(1)
            curr.next = prev            # O(1)
            prev = curr                 # O(1)
            curr = temp_next            # O(1)
        return prev  # New head of reversed list

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # Step 1: Handle edge cases
        # Time: O(1)
        if head is None or head.next is None:
            return head

        # Step 2: Use slow and fast pointers to find the middle of the list
        # Time: O(n)
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Step 3: Reverse second half of the list
        # Time: O(n)
        second = self.reverse(slow.next)
        slow.next = None  # Cut off the first half

        # Step 4: Merge the two halves
        # Time: O(n)
        first = head
        while second:
            temp1, temp2 = first.next, second.next  # O(1)
            first.next = second  # Link from first half to second half
            second.next = temp1  # Link back to remaining first half
            first = temp1
            second = temp2

"""
Time Complexity Analysis:
- Finding middle with slow/fast: O(n)
- Reversing second half: O(n)
- Merging both halves: O(n)
- Total Time Complexity: O(n)

Space Complexity Analysis:
- Only a few pointers used (slow, fast, curr, prev, etc.)
- No extra data structures used
- Total Space Complexity: O(1)
"""
