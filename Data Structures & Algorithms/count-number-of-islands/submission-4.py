class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]

        def dfs(row, col):
            grid[row][col] = "0"
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if (r >= 0 
                and c >= 0 
                and r < rows 
                and c < cols 
                and grid[r][c] == "1"):
                    dfs(r, c)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    dfs(row, col)
                    islands += 1
        return islands
