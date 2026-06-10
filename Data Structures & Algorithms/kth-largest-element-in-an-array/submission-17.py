class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def part(l, r):
            pivot, i = nums[r], l

            for j in range(l, r):
                if nums[j] < pivot: #< or <=
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[r], nums[i] = nums[i], nums[r]
            return i

        def kthlargest(l, r):
            while l <= r:
                kth = part(l, r)

                if kth + 1 == k:
                    return nums[kth]
                if kth + 1 < k:
                    l = kth + 1
                if kth + 1 > k:
                    r =  kth -1
            
            
        k = len(nums) -k + 1
        return kthlargest(0, len(nums)-1)
    