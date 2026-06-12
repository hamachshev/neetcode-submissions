class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def pali(word):
            l, r = 0, len(word) -1
            while l <= r:
                if word[l] != word[r]: return False
                l += 1
                r -= 1
            return True

        def recurse(i, word, part):
            if i == len(s): 
                if word:
                    if pali(word):
                        part.append(word)
                        res.append(part[:])
                        part.pop()
                return

            #split
            if pali(word + s[i]):
                part.append(word + s[i])
                recurse(i + 1, "", part)
                part.pop()
            
            # add to word
            recurse(i + 1, word + s[i], part)
            
        recurse(0, "", [])
        return res

