class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        island = 0
        def dfs(r,c):
            if (r>=rows or c>=columns or r<0 or c<0 or grid[r][c]=="0"):
                return
            grid[r][c]="0"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1":
                    dfs(r,c)
                    island+=1
        return island