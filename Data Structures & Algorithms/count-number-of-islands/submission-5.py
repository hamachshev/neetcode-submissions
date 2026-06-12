class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        q = deque()
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
        def bfs():
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r >= 0 and 
                    c >= 0 and 
                    r < len(grid) and 
                    c < len(grid[0]) and 
                    grid[r][c] == "1"):
                        grid[r][c] = "0"
                        q.append((r,c))

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    grid[row][col] = "0"
                    q.append((row, col))
                    bfs()
                    islands += 1
        return islands
                    