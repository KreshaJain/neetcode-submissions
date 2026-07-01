class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        maps = {i:[] for i in range(numCourses)}
        for i,j in prerequisites:
            maps[i].append(j)
        visit = set()
        def dfs(i):
            if i in visit:
                return False
            if maps[i] == []:
                return True
            visit.add(i)
            for pre in maps[i]:
                if not dfs(pre):
                    return False
            visit.remove(i)
            maps[i] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True