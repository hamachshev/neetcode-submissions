class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def recurse(i, sub):
            if i >= len(nums):
                return res.append(sub.copy())
            
            sub.append(nums[i])
            recurse(i + 1, sub)
            sub.pop()

            recurse(i + 1, sub)
        
        recurse(0, [])
        return res
                
                

            
