class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea, area = 0, 0
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]

        def dfs(row, col):
            nonlocal area
            grid[row][col] = 0
            area += 1

            for dr, dc in directions:
                r, c = row + dr, col + dc
                if (r >= 0 and
                c >= 0 and
                c < cols and
                r < rows and 
                grid[r][c] == 1
                ):
                    dfs(r, c)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    dfs(row, col)
                    maxArea = max(area, maxArea)
                    area = 0
        return maxArea