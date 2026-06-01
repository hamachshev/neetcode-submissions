class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        _dict = defaultdict(list)
        for string in strs:
            sortString = "".join(sorted(string))
            _dict[sortString].append(string)
        return list(_dict.values())