class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        maps = {i:[] for i in range(numCourses)}
        for i,j in prerequisites:
            maps[i].append(j)
        res = []
        visit,compl = set(),set()
        def dfs(i):
            if i in visit:
                return False
            if i in compl:
                return True
            visit.add(i)
            for pre in maps[i]:
                if not dfs(pre):
                    return False
            visit.remove(i)
            compl.add(i)
            res.append(i)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res

        