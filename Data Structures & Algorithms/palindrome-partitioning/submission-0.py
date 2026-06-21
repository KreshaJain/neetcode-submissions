class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        final=[]
        def dfs(i,j):
            if i==len(s):
                if i == j:
                    res.append(final.copy())
                return
            if self.checkpal(s,i,j):
                final.append(s[j:i+1])
                dfs(i+1,i+1)
                final.pop()
            dfs(i+1,j)
        dfs(0,0)
        return res
    def checkpal(self,s,j,i):
        while i<j:
            if s[i] != s[j]:
                return False
            i = i+1
            j = j-1
        return True
