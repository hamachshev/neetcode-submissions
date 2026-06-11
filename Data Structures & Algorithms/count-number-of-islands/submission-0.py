class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def checkn(row, col):
            
            if grid[row][col] != "1": return 
            if (row, col) in seen: return
 
            seen.add((row, col))
            

            
            if row + 1 < rows:
                checkn(row + 1, col)
            if row - 1 >= 0:
                checkn(row -1, col)
            if col + 1 < cols:
                checkn(row, col + 1)
            if col - 1 >= 0:
                checkn(row, col - 1)

            return True
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                print(row, col)
                if checkn(row, col):
                    islands += 1
        return islands
            
            
        
                