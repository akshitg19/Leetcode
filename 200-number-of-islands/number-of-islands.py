class Solution:
    # Akshit
    def dfs(self, grid, r, c):
        grid[r][c] = '0'
        lst = [(r, c - 1), (r, c + 1), (r - 1, c), (r + 1, c)]
        for rows, cols in lst:
            if rows >= 0 and rows < len(grid) and cols >= 0 and cols < len(grid[rows]) and grid[rows][cols] == '1':
                self.dfs(grid,rows,cols)

    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '1':
                    self.dfs(grid, r, c)
                    islands +=1
        return islands

        