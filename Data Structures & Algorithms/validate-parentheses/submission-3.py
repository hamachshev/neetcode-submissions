class Solution:
    def isValid(self, s: str) -> bool:
        map = {'}': '{', ')':'(',']':'['}
        stack = []

        for char in list(s):
            if char not in map:       
                stack.append(char)
            else:
                if not stack or stack.pop() != map[char]:
                    return False
        return not stack 