class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        curr = ""
        def dfs(row, col):
            nonlocal curr
            curr += board[row][col]
            if curr == word: return True

            for dr, dc in directions:
                r, c = row + dr, col + dc
                if (r >= 0 and
                r < rows and
                c >= 0 and
                c < cols and
                len(curr) < len(word) and 
                board[r][c] == word[len(curr)]
                ):
                    tmp = board[row][col]
                    board[row][col] = ""
                    
                    if dfs(r, c): return True
                    
                    board[row][col] = tmp
            curr = curr[:-1]
            return False
            
        for row in range(rows):
            for col in range(cols):
                if dfs(row, col):
                    return True

        return False