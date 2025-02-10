"""

Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. 
If it doesn't exist, return -1 for this number.


Example 1:

Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.

Example 2:

Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]
 

Constraints:

1 <= nums.length <= 104
-109 <= nums[i] <= 109


Time Complexity: O(n) - Each element is pushed and popped from the stack at most once.
Space Complexity: O(n) - The result array and stack can each hold up to n elements.

Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this : No

"""


# Approach: 
# used a monotonic decreasing stack to keep track of indices whose next greater element is not yet found. 
# iterated through the array twice to simulate the circular nature, popping elements from the stack when a greater element is found. 
# The stack stores indices only from the first pass, ensuring each element is processed efficiently.


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        res = [-1] * n
        stack = []  

        for i in range(2 * n):  # Iterate twice to simulate circular array
            while stack and nums[i % n] > nums[stack[-1]]:
                res[stack.pop()] = nums[i % n]
            
            if i < n:  # Only push indices from the first pass
                stack.append(i % n)
        
        return res

