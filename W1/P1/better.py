"""
This has 2 loops, where outer loop fixes the first element
and the second loop acts as if we are dealing with 2 Sum problem using two-pointer technique
There is an overhead, where we check whether a particular triplet already exists or not and,
accordingly we include the triplet. This is done to eliminate duplicates.
"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        result = []
        nums.sort()

        for i in range(0, n - 2):
            first = nums[i]
            j, k = i + 1, n - 1

            while j < k:
                second = nums[j]
                third = nums[k]

                two_sum = second + third

                if ((first + two_sum) > 0):
                    k = k - 1
                elif ((first + two_sum) < 0):
                    j = j + 1
                else:
                    triplet = [first, second, third]
                    if triplet not in result:
                        result.append(triplet)
                    
                    k = k - 1
                    j = j + 1

        return result