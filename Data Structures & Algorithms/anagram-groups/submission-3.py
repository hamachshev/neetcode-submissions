class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        _dict = defaultdict(list)

        for string in strs:
            _dict["".join(sorted(string))].append(string)
        
        return list(_dict.values())
