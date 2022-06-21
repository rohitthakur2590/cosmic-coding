"""
Problem:
  - Find longest substring without repeating.
  input: = [a,b,c,a,b,c,a,a]
  output: 3
"""


class Solution:

    def find_substring(self, data):
        """
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param data:
        :return:
        """
        max_sub = 0

        l = 0
        r = 0
        hm = {}
        max_sub = 0
        while r < len(data):
            if data[r] not in hm:
                hm[data[r]] = r
            else:
                l += 1
                hm[data[r]] = r
            max_sub = max(max_sub, r-l+1)
            r += 1
        return max_sub

    def max_substring(self, data):
        """
        Time Complexity: O(N)
        Space Complexity: O(N
        :param data:
        :return:
        """

        max_substr = 0
        l = 0
        r = 0
        hmaps = {}

        while r < len(data):
            el = data[r]
            if el in hmaps:
                l = hmaps[el] + 1
            hmaps[el] = r
            max_substr = max(max_substr, (r-l +1))
            r += 1

        return max_substr


sol = Solution()

inputs = ["abcabcaa", "", "a", "aa", "aaaa", "ab"]

for input in inputs:
    print("Longest substring for ", input, " : ", sol.find_substring(input))

print("------------------------------------------------------------------")
for input in inputs:
    print("Longest substring for ", input, " : ", sol.max_substring(input))