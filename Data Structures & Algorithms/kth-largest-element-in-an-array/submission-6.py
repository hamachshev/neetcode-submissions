class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k + 1

        def help(nums, k):
            pivot = nums[len(nums)//2]

            lower = [x for x in nums if x < pivot]
            middle = [x for x in nums if x == pivot]
            higher = [x for x in nums if x > pivot]

            if len(lower) >= k:
                return help(lower, k)

            if len(lower) + len(middle) < k:
                return help(higher, k - len(lower) - len(middle))
        
            return pivot 
        return help(nums, k)
    