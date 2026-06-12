class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def recurse(i, comb, total):
            if total > target: return
            if total == target: return res.append(comb[:])

            for j in range(i, len(candidates)):
                choice = candidates[j]
                comb.append(choice)
                recurse(j, comb, total + choice)
                comb.pop()

                
        recurse(0, [], 0)
        return res
