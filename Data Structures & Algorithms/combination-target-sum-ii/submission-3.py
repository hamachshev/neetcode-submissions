class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sub = []
        res = []
        candidates.sort()

        def dfs(i, total):
            if total == target: 
                return res.append(sub[:])
            if i >= len(candidates) or total > target: return

            #choose
            
            sub.append(candidates[i])
            dfs(i + 1, total + candidates[i])
            sub.pop()

            #skip
            while i + 1 < len(candidates) and (candidates[i] == candidates[i+1]):
                i += 1
            dfs(i + 1, total)
        
        dfs(0, 0)
        return res
