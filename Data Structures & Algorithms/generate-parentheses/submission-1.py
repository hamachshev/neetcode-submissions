class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        def recurse(arr, open, n):
            if n == 0:
                res.append("".join(arr))
                return
            
            if not open:
                arr.append("(")
                recurse(arr, open + 1, n)
                arr.pop()
                return

            if n == open:
                arr.append(")")
                recurse(arr, open - 1, n - 1)
                arr.pop()
                return
                
            
            
            arr.append("(")
            recurse(arr, open +1, n)

            arr.pop()

            if open:
                arr.append(")")
                
                recurse(arr, open -1 , n - 1)
                arr.pop()
                
                
        recurse([], 0, n )
        return res
            


            
