class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        open = 0
        res = []
        def recurse(arr, n):
            nonlocal open
            if n == 0:
                res.append("".join(arr))
                return
            
            if not open:
                arr.append("(")
                open += 1
                recurse(arr, n)
                arr.pop()
                open -= 1
                return

            if n == open:
                arr.append(")")
                open -= 1
                recurse(arr, n - 1)
                arr.pop()
                open += 1
                return
                
            
            
            arr.append("(")
            open += 1
            recurse(arr, n)

            arr.pop()
            open -= 1

            if open:
                arr.append(")")
                open -= 1
                recurse(arr, n - 1)
                arr.pop()
                open += 1
                
                
        recurse([], n )
        return res
            


            
