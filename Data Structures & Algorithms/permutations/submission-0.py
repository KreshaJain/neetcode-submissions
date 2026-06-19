class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res =[]
        def dfs(cur):
            if len(cur)==len(nums):
                res.append(cur.copy())
            for j in nums:
                if j in cur:
                    continue
                cur.append(j)
                dfs(cur)
                cur.pop()
        dfs([])
        return res
            