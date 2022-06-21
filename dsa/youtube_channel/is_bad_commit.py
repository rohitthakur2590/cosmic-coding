"""
Problem:
  - Find out the first BAD commit.


"""
class Solution:
    def statusBad(self, commit):
        if commit > 5:
            return True
    def is_badCommit(self, commits):
        """
        Time Complexity:
        Space Complexity:
        :param commits:
        :return:
        """

        # commits = [1,2,3,4,5,6,7,8]
        r = len(commits)
        l = 0

        while l < r:
            mid = (l+r)//2
            if self.statusBad(commits[mid]):
                r = mid
            else:
                l = mid + 1

        return commits[l]

sol = Solution()
inputs = [[1,2,3,4,5,6,7],]

for input in inputs:
    print("Bad Commit: ", sol.is_badCommit(input))
