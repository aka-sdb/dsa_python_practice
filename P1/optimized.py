"""
This has 2 loops, like the better.py file here also we use the two-pointer technique.
Here, we remove the duplicate check overhead by simply moving the pointers.
If either x or y position's value is the same as their previous values, then keep on
moving the pointers till the values differ.
"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        result = []
        nums.sort()

        for i in range(0, n - 2):
            first = nums[i]
            if (i > 0) and (first == nums[i - 1]):
                continue
            
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
                    result.append(triplet)
                    
                    j = j + 1
                    while (nums[j] == nums[j - 1]) and (j < k):
                        j = j + 1

                    k = k - 1
                    while (nums[k] == nums[k + 1]) and (j < k):
                        k = k - 1

        return result