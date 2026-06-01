class Solution:
    def isValid(self, s: str) -> bool:
        map = {'}': '{', ')':'(',']':'['}
        stack = []

        for char in list(s):
            if char not in map:       
                stack.append(char)
            else:
                if len(stack) == 0 or stack.pop() != map[char]:
                    return False
        return len(stack) == 0 