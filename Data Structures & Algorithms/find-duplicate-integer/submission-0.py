class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        _set = set()

        for num in nums:
            if num in _set:
                return num
            _set.add(num)