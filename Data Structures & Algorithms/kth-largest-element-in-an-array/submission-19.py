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
            
                if i == k:
                    return nums[i]
                if i < k:
                    l = i + 1
                if i > k:
                    r =  i -1
            
            
        k = len(nums) -k 
        return qselect(0, len(nums)-1)
    