"""
Problem:
  Description: Find maximum sum for k size window and array elements

  Input:
    - arr = [1,4,3,7,6,5], k = 3

  Output:
    - 18 (7+6+5)
"""
class Solution:
    def maximum_kwin_sum(self, arr, k):
        """
        Time Complexity:  O(N*K)
        Space Complexity: O(1)
        :param arr:
        :param k:
        :return:
        """
        if len(arr) < k:
            print("Error: window size exceeds length of Array!")
            return
        max_sum = 0
        l = 0

        while l <= (len(arr)-k):  # (O(N-K))
            win_sum = sum(arr[l:l+k]) # (O(K))
            max_sum = max(max_sum, win_sum)
            l += 1

        return max_sum

sol = Solution()
arr = [1,4,3,-7,6,5]

print("maximum win size 1 sum: ", sol.maximum_kwin_sum(arr,1))
print("maximum win size 2 sum: ", sol.maximum_kwin_sum(arr,2))
print("maximum win size 3 sum: ", sol.maximum_kwin_sum(arr,3))
print("maximum win size 4 sum: ", sol.maximum_kwin_sum(arr,4))
print("maximum win size 5 sum: ", sol.maximum_kwin_sum(arr,5))
print("maximum win size 6 sum: ", sol.maximum_kwin_sum(arr,6))
print("maximum win size 7 sum: ", sol.maximum_kwin_sum(arr,7))
