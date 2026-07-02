class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        maps = {i:[] for i in range(n)}
        for i,j in edges:
            maps[i].append(j)
            maps[j].append(i)
        visit=set()
        def dfs(node):
            visit.add(node)
            for neigh in maps[node]:
                if neigh not in visit:
                    dfs(neigh)
        count = 0
        for i in range(n):
            if i not in visit:
                dfs(i)
                count+=1
        return count      