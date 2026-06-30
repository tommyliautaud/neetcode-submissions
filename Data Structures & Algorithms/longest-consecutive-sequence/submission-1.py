class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = sorted(nums)       
        cur_max = 1
        max = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                cur_max += 1
                if cur_max > max:
                    max = cur_max
            elif nums[i] > nums[i - 1]:
                cur_max = 1
        return max
            