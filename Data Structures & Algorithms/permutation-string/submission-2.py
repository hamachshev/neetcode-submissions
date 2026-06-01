class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        _dict = {}
        left = 0

        for char in s1:
            _dict[char] = _dict.get(char, 0) + 1
        
        for right in range(len(s2)):
            if s2[right] in _dict:
                _dict[s2[right]]-=1
                if _dict[s2[right]] == 0:
                    del _dict[s2[right]]
                if len(_dict) == 0:
                    return True
            else:
                while left != right:
                    if s2[left] == s2[right]:
                        break
                    _dict[s2[left]] = _dict.get(s2[left], 0) + 1
                    left += 1
                left+=1
            
        return False