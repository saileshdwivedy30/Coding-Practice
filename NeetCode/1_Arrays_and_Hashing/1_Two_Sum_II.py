class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        Approach 1: Bruteforce -

            - For each number need to traverse the array to find the matching sum pair.

                TC: O(n)
                SC: O(1)

        Appraoch 2: Optimal - 

            - Spot Pattern : Array is sorted and we need to search based on a condition => Two pointer, one from front and one from back
            - Movement condition = Compare running sum and target
            - end = end - 1  when sum > target else start = start + 1

                TC: O(n)
                SC: O(1)

        '''
        start = 0
        end = len(numbers)-1
        
        while start<end:

            curr_sum = numbers[start]+numbers[end]

            if curr_sum == target:
                return [start+1,end+1]
            elif curr_sum > target:
                end = end - 1
            else:
                start = start + 1
        return []


















