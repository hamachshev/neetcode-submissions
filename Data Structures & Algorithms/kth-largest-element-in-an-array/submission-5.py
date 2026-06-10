class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def help(nums, k):
            pivot = nums[len(nums)//2]

            lower = [x for x in nums if x < pivot]
            middle = [x for x in nums if x == pivot]
            higher = [x for x in nums if x > pivot]

            if len(higher) >= k:
                return help(higher, k)

            if len(higher) + len(middle) >= k:
                return pivot
            return help(lower, k - len(higher) - len(middle))
        
        return help(nums, k)
    