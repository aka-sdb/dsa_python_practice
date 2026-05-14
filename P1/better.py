"""
This has 2 loops, where outer loop fixes the first element
and the second loop acts as if we are dealing with 2 Sum problem using two-pointer technique
"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        result = []
        nums.sort()

        for i in range(0, n - 2):
            first = nums[i]
            x, y = i + 1, n - 1

            while x < y:
                second = nums[x]
                third = nums[y]

                two_sum = second + third

                if ((first + two_sum) > 0):
                    y = y - 1
                elif ((first + two_sum) < 0):
                    x = x + 1
                else:
                    triplet = [first, second, third]
                    if triplet not in result:
                        result.append(triplet)
                    
                    y = y - 1
                    x = x + 1

        return result