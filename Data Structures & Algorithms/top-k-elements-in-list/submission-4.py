class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        _dict = defaultdict(int)

        for num in nums:
            _dict[num] += 1
        
        return [x[0] for x in sorted(_dict.items(),key=lambda x: x[1],reverse=True)][:k]