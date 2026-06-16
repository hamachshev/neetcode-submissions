class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        rows, cols = len(heights), len(heights[0])
        atl, pacific = set(), set()
        res = []

        def dfs(row, col, seen):
            seen.add((row, col))
            for dr, dc in directions:
                r, c  = row + dr ,col + dc
                if (
                    r >= 0 and
                    c >= 0 and
                    c < cols and
                    r < rows and
                    heights[r][c] >= heights[row][col] and
                    (r, c) not in seen
                ):
                    dfs(r, c, seen)
        
        for row in range(rows):
            dfs(row, 0, pacific)
            dfs(row, cols -1, atl)
        
        for col in range(cols):  
            dfs(0, col, pacific)
            dfs(rows -1, col, atl)
        for row in range(rows):
            for col in range(cols):
                if (row, col) in atl and (row, col) in pacific:
                    res.append([row, col])

        return res


