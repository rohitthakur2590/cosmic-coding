"""
Problem:
  - Given an array of integers, write a function to move all 0's to the end while maintaining
  - the relative order of other elements

Example:
    input:
      - arr =  [0,1,0,3,12]
    expected_output:
      - arr = [1,3,12]

"""
class Solution:
    def move_zero_brute_force(self, arr):
        """
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param arr:
        :return:
        """
        for i in range(len(arr)):
            if arr[i] == 0:
                j = i +1
                while j < (len(arr)-1) and arr[j] == 0:
                    j += 1
                if j < len(arr):
                    arr[i], arr[j] = arr[j], arr[i]

        return arr

    def move_zero_optimize(self, arr):
        """
        Time Complexity: O(N) + O(M) => O(N)
        Space Complexity: O(1)
        :param arr:
        :return:
        """
        j = 0
        for num in arr:
            if num != 0:
                arr[j] = num
                j += 1
        for i in range(j, len(arr)):
            arr[i] = 0
        return arr


sol = Solution()
arr = [0, 1, 0, 3, 12]
arr = sol.move_zero_brute_force(arr)

print("Brute_Force:", arr)
arr = [0, 1, 0, 3, 12]
arr = sol.move_zero_optimize(arr)

print("Optimize: ", arr)

