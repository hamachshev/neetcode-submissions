class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq  = defaultdict(int)
        res = []

        for num in nums:
            freq[num] +=1
        
        temp = []
        for key, value in freq.items():
            temp.append([value, key])
        temp.sort(reverse=True)

        for i in range(k):
            res.append(temp[i][1])
            
        return res



        


        