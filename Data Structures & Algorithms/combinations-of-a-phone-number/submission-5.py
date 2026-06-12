class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not digits: return res
        keypad = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def recurse(i, word):
            if i == len(digits):
                return res.append(word)
            
            for letter in keypad[digits[i]]:
                recurse(i + 1, word + letter)
        recurse(0, "")
        return res
