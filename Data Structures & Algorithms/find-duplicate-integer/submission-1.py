class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = 0

        for num in nums:
            if not seen & (1 << num) :
                seen |=  1 << num
            else:
                return num