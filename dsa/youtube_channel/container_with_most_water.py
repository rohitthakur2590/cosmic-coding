"""
Problem:
  - you are given an integer array of length n.
    there are n verticle lines drawn such that the two end points of
    the ith line are (i,0) & (i, height[i])
  - find two lines that together with x-axis form a container, such that container contains the most water.
  - Return maximum amount of water a container can store.

Solution:
  - height array can't be of length less thatn 2

"""

class Solution:
    def brute_force(self, heights):
        """
        Time Complexity: O(N2)
        Space Complexity: O(1)
        :param heights:
        :return:
        """

        if len(heights) < 2:
            print("Array should have atleast two elements")
            return
        length = len(heights)
        max_water = 0
        for i in range(length-1):
            for j in range(i+1, length):
                max_water = max(max_water, min(heights[i], heights[j]) * (j-i))

        return max_water

    def optimized(self, heights):
        """
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param heights:
        :return:
        """
        if len(heights) < 2:
            print("Index should have at least two elements")
            return
        max_water = 0
        l = 0
        r = len(heights)-1

        while l<r:
            max_water = max(max_water, min(heights[l], heights[r]) * (r-l))
            if l < r:
                l += 1
            else:
                r -= 1

sol = Solution()
inputs = [[1,0,7,4,3,2], [1,0,7,8,3,2], [1,0,0,0,0,0], [1,0,-1,0,0,0], [1]]

for input in inputs:
    print("Max Water for ", input, ": ", sol.brute_force(input))

print("******************************")

for input in inputs:
    print("Max Water for ", input, ": ", sol.optimized(input))
