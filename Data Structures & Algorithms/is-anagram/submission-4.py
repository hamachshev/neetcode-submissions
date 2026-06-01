class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        _dict  = defaultdict(int)

        for char in s:
            _dict[char] += 1

        for char in t:
            if _dict[char] == 0:
                return False
            _dict[char] -= 1
        return True

            
