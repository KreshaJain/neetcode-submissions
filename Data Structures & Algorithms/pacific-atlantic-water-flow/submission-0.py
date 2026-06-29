class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows,columns = len(heights),len(heights[0])
        pac,atl = set(),set()
        def dfs(r,c,vis,prev):
            if((r,c)in vis or r<0 or c<0 or r>= rows or c>= columns or heights[r][c]<prev):
                return
            vis.add((r,c))
            dfs(r+1,c,vis,heights[r][c])
            dfs(r-1,c,vis,heights[r][c])
            dfs(r,c+1,vis,heights[r][c])
            dfs(r,c-1,vis,heights[r][c])
        for r in range(rows):
            dfs(r,0,pac,heights[r][0])
            dfs(r,columns-1,atl,heights[r][columns-1])
        for c in range(columns):
            dfs(0,c,pac,heights[0][c])
            dfs(rows-1,c,atl,heights[rows-1][c])
        res=[]
        for r in range(rows):
            for c in range(columns):
                if (r,c) in pac and (r,c) in atl:
                    res.append((r,c))
        return res