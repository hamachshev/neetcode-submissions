class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = set()
        def check_pos(board: List[List[str]], word: str, row: int, col: int):
            if not word: return True
            if (row, col) in seen: return False
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]): return False

            if board[row][col] == word[0]:
                seen.add((row, col))
                word1 = "".join(word[1:])
                if (check_pos(board, word1, row + 1, col) or 
                check_pos(board, word1, row, col + 1) or 
                check_pos(board, word1, row - 1, col) or 
                check_pos(board, word1, row, col -1)
                ): return True
                else:
                    seen.remove((row, col))
                    return False
            return False

        for row  in range(len(board)):
            for col in range(len(board[row])):
                if check_pos(board, word, row, col): return True
        return False