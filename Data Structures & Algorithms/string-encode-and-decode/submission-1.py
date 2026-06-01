class Solution:

    def encode(self, strs: List[str]) -> str:
        for i in range(len(strs)):
            strs[i] = str(len(strs[i])) +"#" + strs[i]
        temp = "".join(strs)
        print(temp)
        return "".join(strs)
    
    def decode(self, s: str) -> List[str]:
        res = []
        while len(s) > 0:
            length = ""
            pointer = 0
            while s[pointer] != "#":
                length+= s[pointer]
                pointer +=1
            pointer +=1 
            
            res.append(s[pointer: pointer + int(length)])
            s = s[pointer + int(length):]
        return res


