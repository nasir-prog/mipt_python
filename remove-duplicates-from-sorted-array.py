class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        count = 0
        for value in nums:
            if count == 0 or value != nums[count - 1]:
                nums[count] = value
                count += 1
        return count
