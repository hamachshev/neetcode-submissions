class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []


        def dfs(arr, total, nums):
            if total == target :
                res.append(arr.copy())
                
            if total >= target:
                return
            
            for i in range(len(nums)):
                
                #total += num does not work for some reason
                new = arr.copy()
                new.append(nums[i])
                dfs(new, total + nums[i], nums[i:])

        dfs([], 0, nums)
        return res