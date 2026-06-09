class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []
        nums.sort()
        
        def dfs(i):
            if i >= len(nums):
                return res.append(sub.copy())
                
            sub.append(nums[i])
            dfs(i + 1)
            sub.pop()

            #skipping, must skip all nums[i]
            i += 1
            while i < len(nums) and (nums[i] == nums[i - 1]):
                i += 1
            
            dfs(i)
            

        dfs(0)
        return res