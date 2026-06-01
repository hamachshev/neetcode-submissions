class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _dict = {}

        for i, num in enumerate(nums):
            if target - num in _dict:
                return [_dict[target-num], i]
            _dict[num] = i
        
        return []