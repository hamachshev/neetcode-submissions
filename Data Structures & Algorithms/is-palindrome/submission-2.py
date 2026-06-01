class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left <= right:
            while left < len(s) - 1 and not s[left].isalnum():
                left += 1
            
            while right > 0 and not s[right].isalnum():
                right -= 1
            
            if left <= right and s[left].lower() != s[right].lower():
                return False
            
            right -= 1
            left += 1
        
        return True