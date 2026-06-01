class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for _ in range(9)] 
        rows = [set() for _ in range(9)]
        squares =  [[set() for _ in range(3)] for _ in range(3)]

        for row in range(9):
            for col in range(9):
                element = board[row][col]
                if element == ".": continue

                if element in cols[col] or element in rows[row] or element in squares[row//3][col//3]:
                    return False
                cols[col].add(element)
                rows[row].add(element)
                squares[row//3][col//3].add(element)
        return True