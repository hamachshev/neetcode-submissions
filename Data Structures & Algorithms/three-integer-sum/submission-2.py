class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            left, right = i + 1, len(nums) -1

            if i > 0 and nums[i - 1] == nums[i]:
                continue
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    while left < right and nums[right] == nums[right -1]:
                        right -= 1
                    while left < right and nums[left] == nums[left + 1]:
                        left +=1 
                    res.append([nums[i], nums[left], nums[right]])
                    right -= 1
                    left += 1
        return res
                
