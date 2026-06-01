class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        _dict = {}
        res = []

        for string in strs:
            key = ''.join(sorted(string))
            if key not in _dict:
                _dict[key] = []
            _dict[key].append(string)

        for value in _dict.values():
            res.append(value)
        return res