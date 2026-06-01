class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _dict = {}

        for i in range(len(nums)):
            other = target - nums[i]
            if other in _dict:
                return [_dict[other], i]
            
            _dict[nums[i]] = i

        