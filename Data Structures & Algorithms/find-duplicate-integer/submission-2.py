class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #after looking at solution, trying to implement without lookiung at code
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                return abs(num)
            nums[idx] *= -1