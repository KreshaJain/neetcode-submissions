class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        for k in range(len(edges)-1,-1,-1):
            maps = {i:[] for i in range(len(edges)+1)}
            for idx,(u,v) in enumerate(edges):
                if idx == k:
                    continue
                maps[u].append(v)
                maps[v].append(u)
            visit = set()
            def dfs(node,parent):
                visit.add(node)
                for neigh in maps[node]:
                    if neigh == parent:
                        continue
                    if neigh in visit:
                        return False
                    if not dfs(neigh,node):
                        return False
                return True
            if dfs(1, -1) and len(visit) == len(edges):
                return edges[k]


