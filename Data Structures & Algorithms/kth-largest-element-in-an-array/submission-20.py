class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)

        for num in nums[k:]:
            heapq.heappush(heap,num)
            if len(nums) > k:
                heapq.heappop(heap)
     
        return heap[0]