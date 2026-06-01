class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _dict = {}

        for i,num in enumerate(nums):
            find = target - num
            if find in _dict:
                return [_dict[find], i]
            _dict[num] = i
        return []