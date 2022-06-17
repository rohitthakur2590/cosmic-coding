"""
Problem:
  - Given an array people and an integer limit. People array is an array of peoples weights
  - ith person has a weight people[i] and each boat can carry at most limit.
  - Each boat can carry at most two people at the same time, given that their weight sum is at most limit.
  - returns the minimum no. of boats to carry every given person.
Solution:
  - weights can not be negative
  - maximum people boat can have two
  - individual weight can't exceed max weight capacity of boat
  - weight array can't be empty

"""
class Solution:
    def cound_needed_boats(self, weights, limit):
        """
        Time Complexity: O(NlogN)
        Space Complexity: O(N)
        :param weights:
        :param limit:
        :return: needed_boat_count
        """
        l = 0
        h = len(weights) - 1
        needed_boat_count = 0
        weights.sort()   # O(NLogN) ans also S.C => O(N)
        while l <= h:
            if (weights[l] + weights[h]) <= limit:
                l += 1
                h -= 1
            else:
                h -= 1
            needed_boat_count += 1
        return needed_boat_count


sol = Solution()
weights = [60, 48, 39, 70, 90]

count = sol.cound_needed_boats(weights, 90)
print("Boat Count: ", count)
