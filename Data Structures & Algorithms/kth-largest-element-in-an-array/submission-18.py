class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def qselect(l, r):
            while l <= r:
                pivot, i = nums[r], l

                for j in range(l, r):
                    if nums[j] < pivot: #< or <=
                        nums[i], nums[j] = nums[j], nums[i]
                        i += 1
                nums[r], nums[i] = nums[i], nums[r]
            
                if i + 1 == k:
                    return nums[i]
                if i + 1 < k:
                    l = i + 1
                if i + 1 > k:
                    r =  i -1
            
            
        k = len(nums) -k + 1
        return qselect(0, len(nums)-1)
    