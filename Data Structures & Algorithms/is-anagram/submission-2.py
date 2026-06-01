class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check = {}
        for char in s:
            check[char] = check.get(char, 0) +1
        
        for char in t:
            if char in check:
                check[char] -= 1
                if check[char] == 0:
                    del check[char]
            else:
                return False
        return len(check) == 0
    
        