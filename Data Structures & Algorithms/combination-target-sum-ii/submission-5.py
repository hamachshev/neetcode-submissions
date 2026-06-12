class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def recurse(i, comb, total):
            if total == target:
                return res.append(comb[:])
            if total > target or i == len(candidates): return

            #choose
            comb.append(candidates[i])
            recurse(i + 1,comb, total + candidates[i])
            comb.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            #skip
            recurse(i+1, comb,total)

        recurse(0, [], 0)
        return res