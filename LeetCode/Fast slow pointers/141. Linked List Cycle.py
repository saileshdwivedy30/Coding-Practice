'''

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.



Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.


Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.

'''

from typing import Optional  # For Optional type hinting

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        fast = head  # Fast pointer moves two steps at a time
        slow = head  # Slow pointer moves one step at a time

        # Continue loop only if fast and fast.next exist
        # This prevents accessing attributes on NoneType (avoids crash)
        while fast and fast.next:

            fast = fast.next.next  # Move fast pointer two steps
            slow = slow.next       # Move slow pointer one step

            if slow == fast:
                # If both pointers meet, a cycle exists
                return True

        # If loop ends, no cycle was found
        return False

"""
Time Complexity Analysis:
- Both pointers traverse the list at most once
- Fast pointer may complete the loop earlier due to cycle
- Total Time Complexity: O(n), where n is the number of nodes

Space Complexity Analysis:
- Only two pointers used (slow and fast)
- No extra data structures
- Total Space Complexity: O(1)
"""
