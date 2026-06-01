class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t): return False

        _dict = defaultdict(int)

        for x in s:
           _dict[x] += 1
        
        for x in t:
            if not x in _dict:
                return False

            if _dict[x] > 0:
                _dict[x] -= 1
            else:
                return False

        return True
