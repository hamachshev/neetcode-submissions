class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right

        while left <= right:
            k  = left + (right - left) // 2

            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
            
            if hours > h: # if too small k, make k larger
                left = k + 1
                continue
            #this is a legitamite k
            res = k
            right = k - 1 #see if there is a lower k
        return res 
