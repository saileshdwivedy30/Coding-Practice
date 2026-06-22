# This approach uses two stacks: one for the regular stack and one for tracking the minimum values.
# The push operation adds elements to both stacks and keeps track of the minimum, and the pop operation removes from both.
# The getMin operation returns the top of the minimum stack which always contains the current minimum element.
# TC = O(1) and SC = O(n)

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        # when we push something we need to also update the min stack with the min value
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val) # compare the val with the top of min stack and keep the one that is the smallest
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()