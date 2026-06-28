class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,columns = len(grid),len(grid[0])
        fr = 0
        time = 0
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1:
                    fr +=1
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        while fr>0:
            flag = False
            for r in range(rows):
                for c in range(columns):
                    if grid[r][c] == 2:
                        for dr,dc in dirs:
                            nr,nc = r+dr,c+dc
                            if (nr in range(rows) and nc in range(columns) and grid[nr][nc]==1):
                                grid[nr][nc]=3
                                fr -=1
                                flag = True
            if not flag:
                return -1
            for r in range(rows):
                for c in range(columns):
                    if grid[r][c]==3:
                        grid[r][c]=2
            time += 1
        return time
        