class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0]*len(temperatures)
        stack = [] # [temp,idx]
        
        for idx, temp in enumerate(temperatures):
            # while he curretn temp val is greater than everything in stack
            while stack and temp>stack[-1][0]:
                stackT,stackIdx = stack.pop()
                # add to res the diff of curr idx and when we found the next highest
                res[stackIdx] = idx-stackIdx
            # if not keep adding whatever comes in
            stack.append([temp,idx])
        return res