class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:   
            nums = set()
            for box in row:
                if box != ".":
                    if box in nums: return False
                    nums.add(box)
        
        for i in range(len(board[0])):   
            nums = set()
            for j in range(len(board)):
                box = board[j][i]
                if box != ".":
                    if box in nums: return False
                    nums.add(box)

        nums = [set(), set(), set()]
        for i in range(len(board)):
            if i % 3 == 0:
                nums = [set(), set(), set()]
            for j in range(len(board[0])):
                box = board[i][j]
                if box != ".":
                    if box in nums[j//3]:
                        return False
                    nums[j//3].add(box)
        return True
           


