class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        left, right = 0, len(nums) -1
        prev = nums[0]
        el = 0
        while left <= right:
            mid = left + (right - left) // 2
           
            if nums[mid] < prev:
                prev = nums[mid]
                right = mid - 1
            elif nums[mid] > prev:
                el = mid
                prev = nums[mid]
                left = mid + 1
            else:
                curr = nums[el]
                if nums[el + 1] > curr:
                    return curr
                else:
                    break
        return nums[(el + 1) % len(nums)]     