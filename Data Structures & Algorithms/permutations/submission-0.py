class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def recurse(nums):
            if len(nums) == 0: return [[]]

            perms = recurse(nums[1:])
            new_perms = []
            for perm in perms:
                print(perm)
                for i in range(len(perm) + 1):
                    new = perm[:]
                    new.insert(i, nums[0])
                    new_perms.append(new)
            return new_perms
        return recurse(nums)