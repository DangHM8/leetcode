class Solution(object):
    def numIdenticalPairs(self, nums):
        counts = {}
        result = 0
        for num in nums:
            coup = counts.get(num,0)
            result += coup
            counts[num] = coup + 1
        return result