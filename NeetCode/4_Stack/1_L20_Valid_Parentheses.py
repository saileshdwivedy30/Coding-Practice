class Solution:
    def isValid(self, s: str) -> bool:
        '''
        Time complexity: O(n)
        Space: O(n)
        '''
        stack = []
        close_to_open = {')':'(','}':'{',"]":'['}

        # traverse tgough the string
        for c in s:

            # check if closing bracket, then see if in stack else means it aint the closing bracket with the paired oepn bracket we looking for
            if c in close_to_open:
                if stack and stack[-1]==close_to_open[c]:
                    stack.pop()
                else:
                    return False
            # if not closing bracket then append to stack
            else:
                stack.append(c)

        # if stack is empty then we found all matching
        return True if not stack else False
        