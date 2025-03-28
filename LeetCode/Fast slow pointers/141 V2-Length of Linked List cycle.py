from typing import Optional

# ----------------------------------------------
# 🚩 Problem: Length of Cycle in a Linked List
#
# Given the head of a singly linked list that contains a cycle,
# return the **length of the cycle**.
#
# A cycle exists if a node's `next` pointer points to a previous node in the list,
# forming a loop. It is guaranteed that the linked list contains a cycle.
#
# Implement the function:
#     def cycleLength(head: Optional[ListNode]) -> int
#
# 🔍 Example:
# Input: head = [3, 2, 0, -4], pos = 1
# Output: 3
# Explanation: The cycle is 2 → 0 → -4 → 2
#
# ✅ Constraints:
# - The number of nodes in the list is in the range [1, 10^4].
# - Node values range from [-10^5, 10^5].
# - The list is guaranteed to contain a cycle.
# ----------------------------------------------

class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next: Optional[ListNode] = None

# Helper to create a linked list with a cycle
def createLinkedListWithCycle(values, pos) -> Optional[ListNode]:
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    cycle_entry = None

    for index in range(1, len(values)):
        current.next = ListNode(values[index])
        current = current.next
        if index == pos:
            cycle_entry = current

    # Create cycle
    if pos == 0:
        cycle_entry = head
    current.next = cycle_entry

    return head

# Test cases
def test_cycleLength():
    test_cases = [
        ([3, 2, 0, -4], 1, 3),   # cycle: 2 → 0 → -4 → 2
        ([1, 2], 0, 2),          # cycle: 1 → 2 → 1
        ([1], 0, 1),             # cycle: 1 → 1
        ([1, 2, 3, 4, 5, 6], 2, 4), # cycle: 3 → 4 → 5 → 6 → 3
    ]

    for i, (nodes, pos, expected) in enumerate(test_cases):
        head = createLinkedListWithCycle(nodes, pos)
        result = cycleLength(head)
        print(f"Test case {i+1}: Expected {expected}, Got {result} → {'✅' if result == expected else '❌'}")

# 🔧 Write your function below:
def cycleLength(head: Optional[ListNode]) -> int:
    fast = head  # Fast pointer moves two steps
    slow = head  # Slow pointer moves one step

    # Important check to avoid NoneType errors
    while fast and fast.next:

        fast = fast.next.next
        slow = slow.next

        # Cycle detected when fast and slow meet
        if slow == fast:

            # Measure cycle length starting from next node
            curr = slow.next
            cycle_length = 1

            # Keep moving until we loop back to the same node (slow)
            while curr != slow:
                # To find the length of the cycle, we start counting from the next node
                curr = curr.next
                cycle_length += 1

            return cycle_length  # Return total length of the cycle

    return 0  # No cycle found


"""
Time Complexity Analysis:
- Detecting the cycle: O(n)
- Measuring the cycle length: O(c), where c is the length of the cycle
- Overall Time Complexity: O(n), since c ≤ n

Space Complexity Analysis:
- Only pointers used (fast, slow, curr): O(1)
- No extra memory or data structures used
- Overall Space Complexity: O(1)
"""

# Run the tests
test_cycleLength()
