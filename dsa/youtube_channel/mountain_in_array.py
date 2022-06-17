"""
Problem:
  - Given an Array of integers return True if the following conditions are
    fulfilled
  - Length of the array is bigger than or equal to 3
  - There exist some index i such that a[0] < a[1] < ... a[i]
  - a[i] > a[i+1] ... > a[a.size -1 ]

Solution:
  - there can be zero as well
  - minimum 3 elements required
  - sample: [], [1], [0,0,0], [1,2,3], [3,2,1], [1,2,1]
"""

class Solution:
    def is_mountain(self, arr):
        """
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param arr:
        :return:
        """
        if len(arr) < 3:
            print("Invalid array length")
            return
        length = len(arr)
        l = 1
        while l < length and arr[l] > arr[l-1]:
            l += 1
        if l == 1 or l == length:
            return False
        while l < length and arr[l] < arr[l-1]:
            l += 1

        return l == length


sol = Solution()

input = [[], [1], [0,0,0], [1,2,3], [1,1,1], [3,2,1], [1,2,1], [1,2,1,2]]

for item in input:
    print("For Input: ",item, "Mountain Exist: ", sol.is_mountain(item))
