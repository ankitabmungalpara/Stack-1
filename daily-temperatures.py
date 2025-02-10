"""

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.

 
Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100


Time Complexity: O(n), as each temperature is pushed and popped from the stack once.
Space Complexity: O(n), for storing indices in the stack in the worst case (strictly decreasing temperatures).

Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this : No

"""


# Approach: 
# used a monotonic decreasing stack to track temperatures and their indices. 
# If the current temperature is higher than the top of the stack, we pop elements and compute the wait time. 
# Finally, we append the current temperature and its index to the stack.



class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)

        stack = [] # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackI = stack.pop()
                res[stackI] = (i-stackI)

            stack.append([t, i])

        return res

