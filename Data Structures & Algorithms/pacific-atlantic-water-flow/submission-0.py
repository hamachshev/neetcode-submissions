class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        seen = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, cols = len(heights), len(heights[0])
        res = []

        def dfs(row, col, oceans):
            if row == 0 or col == 0: oceans.add("p")
            if row == rows -1 or col == cols -1: oceans.add("a")
            
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if (
                    r >= 0 and c >= 0 and
                    r < rows and c < cols and
                    (r, c) not in seen and
                    heights[r][c] <= heights[row][col]
                ):
                    seen.add((r, c))
                    touch = dfs(r, c, oceans)
                    for o in touch:
                        oceans.add(o)


            return oceans
        
        for row in range(rows):
            for col in range(cols):
                seen = set()
                oceans = dfs(row ,col, set())
                if len(oceans ) == 2:
                    res.append([row, col])
        return res