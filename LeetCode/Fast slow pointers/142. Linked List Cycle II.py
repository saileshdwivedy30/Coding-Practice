'''

Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.



Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
Example 2:


Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
Example 3:


Input: head = [1], pos = -1
Output: no cycle
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
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        fast = head  # Fast pointer (moves two steps)
        slow = head  # Slow pointer (moves one step)

        # Phase 1: Detect the cycle using Floyd's algorithm
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                # Cycle detected. Now measure its length.

                curr = slow.next  # Start from the next node
                cycle_length = 1

                while curr != slow:
                    curr = curr.next
                    cycle_length += 1

                # Phase 2: Find the starting node of the cycle
                start = head
                ahead = head

                # Move one pointer ahead by cycle_length steps
                for i in range(cycle_length):
                    ahead = ahead.next

                # Move both pointers one step at a time
                # They will meet at the cycle start
                while start != ahead:
                    start = start.next
                    ahead = ahead.next

                return start  # Starting node of the cycle

        return None  # No cycle found


"""
Time Complexity Analysis:
- Cycle detection: O(n), where n is the number of nodes
- Cycle length calculation: O(c), where c is the length of the cycle
- Finding cycle start: O(n)
- Overall Time Complexity: O(n)

Space Complexity Analysis:
- Uses constant space (pointers only)
- No extra data structures used
- Overall Space Complexity: O(1)
"""

