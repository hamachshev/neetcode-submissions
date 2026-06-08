class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def check(s):
            r,l = 0, len(s) -1
            while r <= l:
                if s[r] != s[l]: return False
                r+=1
                l -=1
            return True

        def recurse(curr, arr, i):
            if i == len(s):
                if check(curr):
                    arr.append(curr)
                    res.append(arr.copy())
                    arr.pop()
                return

            #partition and start new
            if curr and check(curr):
                arr.append(curr)
                recurse(s[i], arr , i + 1)
                arr.pop()

            #check palindrome and continue
            
            recurse(curr + s[i], arr, i +1)

        recurse("", [], 0)
        return res 

