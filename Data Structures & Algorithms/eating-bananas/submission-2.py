class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = max(piles)

        while left <= right:
            if (left + right) // 2 == 0: return rate #ie less than one banana
            
            rate = (left + right)//2
           
            hours = h

            for pile in piles:
                hours -= math.ceil(pile/rate)
            
            if hours < 0:
                left = rate + 1
            elif hours >= 0:
                res = rate
                right = rate - 1
        
        return res