class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2: return len(nums)
        nums.sort()
        max_streak = 0
        streak = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]: continue
            if nums[i] == nums[i - 1] + 1:
                streak += 1
            else:
                max_streak = max(max_streak, streak)
                streak = 1

        return max(max_streak, streak)