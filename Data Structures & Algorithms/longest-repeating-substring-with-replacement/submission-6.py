class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) < k + 1: return(len(s))
        _dict = defaultdict(int)
        max_len = left = 0

        for right in range(len(s)):
            _dict[s[right]] += 1

            while right - left + 1 - max(_dict.values()) > k:
                _dict[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left +1)
        return max_len 