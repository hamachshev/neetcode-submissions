class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq  = defaultdict(int)
        res = {}

        for num in nums:
            freq[num] +=1

        return sorted(freq.keys(), key=lambda x: freq[x], reverse=True)[:k]



        


        