class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        # when encountering signs need to pop twice and do the ops
        # in "-" and "/" order matters
        # when appending put as int so on popping they come opt as int
        # Time complexity: O(n) for traversing the tokens and O(1) for popping and appending to the stack
        # Space complexity: O(n) for the stack
        for c in tokens:
            if c == "+":
                stack.append(stack.pop()+stack.pop())
            elif c == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif c == "*":
                stack.append(stack.pop()*stack.pop())
            elif c == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(c))
        return stack[0]
