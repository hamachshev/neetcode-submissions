class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        _dict = defaultdict(int)

        for c in s:
            _dict[c] += 1
        
        for c in t:
            if c not in _dict: return False
            _dict[c] -= 1
            if _dict[c] == 0:
                del _dict[c]
                
        
        return len(_dict) == 0
           