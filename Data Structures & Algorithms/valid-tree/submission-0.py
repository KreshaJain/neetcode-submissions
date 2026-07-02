class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        maps = {i:[] for i in range(n)}
        for i,j in edges:
            maps[i].append(j)
            maps[j].append(i)
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
        if not dfs(0,-1):
            return False
        return len(visit) == n
            
        