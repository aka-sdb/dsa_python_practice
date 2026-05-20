"""
Brute force solution - 3 nested loops.
Time complexity = O(n^3)
Space complexity = 2 * O(no. of triplets) [As, one list represents a triplet which in turn
                                        is stored inside another list]
"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        result = []
        nums.sort()

        for i in range(0, n - 2):
            first = nums[i]
            for j in range(i + 1, n - 1):
                second = nums[j]
                for k in range(j + 1, n):
                    third = nums[k]

                    if (first + second + third == 0):
                        triplet = [first, second, third]

                        if triplet not in result:
                            result.append(triplet)

        return result