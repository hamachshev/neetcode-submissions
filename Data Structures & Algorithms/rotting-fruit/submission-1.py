class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
       #BFS! from the rotten fruit
        seen = set()
        q = deque()
        minutes = -2 #minus the rotten at the beginning and the last one at the end
        fruit = 0
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fruit += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
                    fruit += 1
        if not fruit: return 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if (r >= 0 and
                c >= 0 and
                c < cols and
                r < rows and
                grid[r][c] != 0 and
                (r, c) not in seen
                ):
                    seen.add((r, c))
                    q.append((r+1, c))
                    q.append((r -1, c))
                    q.append((r, c+1))
                    q.append((r, c -1))

            minutes += 1

        return minutes if len(seen) == fruit else -1