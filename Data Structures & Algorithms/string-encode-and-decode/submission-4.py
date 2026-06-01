class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += string + "`"
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        temp = ""
        for c in s:
            if c != "`":
                temp += c
            else:
                res.append(temp)
                temp = ""
        return res

