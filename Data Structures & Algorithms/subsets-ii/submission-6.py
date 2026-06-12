class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def recurse(i, freq):
            if i == len(nums):
                tmp = []
                for key, value in freq.items():
                    for i in range(value):
                        tmp.append(key)
                res.add(tuple(tmp))
                return
            
            #choose
            freq[nums[i]] += 1
            recurse(i + 1, freq)
            freq[nums[i]] -= 1

            #skip

            recurse(i +1, freq)
        recurse(0, defaultdict(int))
        return [list(z) for z in res]
