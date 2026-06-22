class Solution:
    def isValid(self, s: str) -> bool:
        '''
        Time complexity: O(n)
        Space: O(n) # worst case all open brackets
        '''
        stack = []  # need stack to compare with latest close (ordered)
        CloseToOpen = {")": "("
            , "}": "{",
                       "]": "["}  # for cheking the open and close pairing

        for c in s:
            if c in CloseToOpen:  # we have close backet at hand
                if stack and stack[-1] == CloseToOpen[
                    c]:  # cant have empty stack to compare with a closed bracket and stack top should be matching open
                    stack.pop()
                else:
                    return False
            else:  # if open bracket then append
                stack.append(c)

        return not stack  # if stack has something then false if nothing then great!
































