'''

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.



Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.


Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100

'''


from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head  # Fast pointer will move two steps at a time
        slow = head  # Slow pointer will move one step at a time

        # The loop continues only if fast and fast.next exist
        # We check fast and fast.next to safely do: fast = fast.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # When fast reaches the end, slow will be at the middle node
        return slow


"""
Time Complexity Analysis:
- Fast and slow both traverse the list at most once
- Each iteration moves slow one step and fast two steps
- Total Time Complexity: O(n), where n is the number of nodes

Space Complexity Analysis:
- Only uses two pointers
- No extra memory used
- Total Space Complexity: O(1)
"""
