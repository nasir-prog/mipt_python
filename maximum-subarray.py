class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current = best = nums[0]
        for index in range(1, len(nums)):
            current = max(nums[index], current + nums[index])
            best = max(best, current)
        return best
