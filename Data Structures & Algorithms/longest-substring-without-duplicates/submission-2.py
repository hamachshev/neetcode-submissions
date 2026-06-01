class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left = 0
        _set = set()
        for right in range(len(s)):
            while s[right] in _set:
                _set.remove(s[left])
                left += 1
            
            longest = max(longest, right - left + 1)
            _set.add(s[right])
        return longest
                
