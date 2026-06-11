class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        maxArea = 0
        area = 0
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(row, col):
            nonlocal area
            area += 1

            for dr, dc in directions:
                r, c = row + dr, col + dc
                if (r < 0 or 
                c < 0 or 
                r >= rows or 
                c >= cols or 
                grid[r][c] != 1 or
                (r,c) in seen 
                ):
                    continue
          
                seen.add((r,c))
                dfs(r, c)


        for row in range(rows):
            for col in range(cols):
                if (row, col) not in seen and grid[row][col] == 1: 
                    seen.add((row, col))
                    dfs(row, col)
                    maxArea = max(maxArea, area)
                    area = 0

        return maxArea
                    