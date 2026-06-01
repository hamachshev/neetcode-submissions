class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)] # i originally did [[]] * len(nums) but apparently this copies the refercne to that one array len(nums) times
        freq_map = defaultdict(int)

        for num in nums:
            freq_map[num] += 1
        
        for key, value in freq_map.items():
            freq[value].append(key)
        
        res = []
        pointer = len(freq) -1
        while len(res) < k:
            for item in freq[pointer]:
                if len(res) < k:
                    res.append(item)
            pointer -= 1
        return res


        