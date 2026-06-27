class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,columns = len(grid),len(grid[0])
        vis = set()
        q = deque()
        def bfs(r,c):
            if (r>=rows or c>=columns or r<0 or c<0 or grid[r][c]==-1 or (r,c)in vis):
                return
            vis.add((r,c))
            q.append([r,c])
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 0:
                    q.append([r,c])
                    vis.add((r,c))
        dis = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dis
                bfs(r+1,c)
                bfs(r-1,c)
                bfs(r,c+1)
                bfs(r,c-1)
            dis +=1