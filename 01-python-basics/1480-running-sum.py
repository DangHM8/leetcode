# LeetCode 1480 - Running Sum of 1d Array
# Difficulty: Easy
# Time: O(n)
# Space: O(n)

class Solution:
    def runningSum(self, nums):
        total = 0
        result = []

        for num in nums:
            total += num
            result.append(total)

        return result