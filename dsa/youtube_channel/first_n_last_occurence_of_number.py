"""
Problem:
  - Find first and last occurrence of a target number in array
INPUT: [10,11,11,11,17,18]

Solution:
  - could array be empty => No
  - Numbers always gonna be consecutive => yes
  - Can there be one occurence of number ? => yes
  - Array always gonna have that number => Yes

"""

class Solution:
    def fin_first_n_last_occu(self, arr, target):
        """
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param arr:
        :param target:
        :return:
        """
        if not arr:
            print("Empty Array!!")

        length = len(arr)
        i = 0
        while i < length and arr[i] != target:
            i += 1
        if i == length:
            return -1, -1

        j = length-1
        while j >= i and arr[j] != target:
            j -= 1
        return i, j

    def get_startIndex(self, arr, target):
        # arr = [10, 11, 11, 11, 17, 18]
        if not arr:
            print("Error: Empty Array!")

        l = 0
        r = len(arr) -1

        while l <= r:
            mid = (l+r)//2
            if arr[mid] == target:
                if mid  == 0 or arr[mid-1] != target:
                    return mid
                r = mid - 1
            elif arr[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1

    def get_endIndex(self, arr, target):
        # arr = [10, 11, 11, 11, 17, 18]
        if not arr:
            print("Error: Empty Array!")

        l = 0
        r = len(arr)-1

        while l <= r:
            mid = (l+r)//2
            if arr[mid] == target:
                if mid == (len(arr) -1 ) or arr[mid+1] != target:
                    return mid
                l = mid + 1
            elif arr[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1


    def optimized_solution(self, nums, target):
        """
        Time Complexity: O(LOG N)
        Space Complexity: O(1)
        :param nums:
        :param target:
        :return:
        """
        return(self.get_startIndex(nums, target), self.get_endIndex(nums, target))

sol = Solution()

inputs = [[10,11,11,11,17,18], [11], [11,11,11,11], []]

for input in inputs:
    print("Start and End position for 11", sol.fin_first_n_last_occu(input, 11))

print("----------------------------------------------------------------------------")

for input in inputs:
    print("Start and End position for 11", sol.optimized_solution(input, 11))


