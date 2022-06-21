"""
Problem:
  - description: Find missing numbers
Solution:
  - can array be wmpty ?
  - can there be negative numbers ?
  - are numbers always gonna be in order ?
"""

class Solution:
    def bruteforce(self, nums):
        """
        Time Complexity: 2*O(N)
        Space Complexity: O(N)
        :param nums:
        :return:
        """
        hm = set()

        # for num in nums:
        #     hm.add(num)
        #
        # for i in range(len(nums) + 1):
        #     if i not in hm:
        #         return i
        for i in range(len(nums) + 1):
            if i not in nums:
                return i


    def optimized_approach(self, nums):
        n = len(nums)
        curr_sum = sum(nums)

        son = (n * (n + 1)) // 2

        return son - curr_sum

sol = Solution()
inputs = [[0,1,3], [1,2,3], [0,1,2,3,4] ]

for input in inputs:
    print("Missing Number: ", sol.bruteforce(input))
print("-----------------------------------------------------")
for input in inputs:
    print("Missing Number: ", sol.optimized_approach(input))