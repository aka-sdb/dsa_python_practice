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