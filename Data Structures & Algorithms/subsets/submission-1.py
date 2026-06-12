class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def recurse(i, sub):
            if i == len(nums):
                res.append(sub[:])
                return
            
            #include
            sub.append(nums[i])
            recurse(i+1, sub)
            sub.pop()

            #exclude

            recurse(i+1, sub)
        
        recurse(0, [])
        return res
