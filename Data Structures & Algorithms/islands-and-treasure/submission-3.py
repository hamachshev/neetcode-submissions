class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        seen = set()
        q = deque()
        inf = 2147483647

        for row in range(rows):
            for col in range(cols):
                if grid[row][col]== 0:
                    q.append((row, col))

        steps = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if (
                    r >= 0 and
                    c >= 0 and
                    r < rows and
                    c < cols and 
                    (r, c) not in seen and
                    grid[r][c] != -1
                ):
                    grid[r][c] = steps
  
                    seen.add((r, c))
                    q.append((r + 1, c))
                    q.append((r -1, c))
                    q.append((r, c + 1))
                    q.append((r, c - 1))

            steps += 1
