class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot %2!=0:
            return False
        target = tot//2
        n = len(nums)
        mem = [[-1]*(target+1) for _ in range(n+1)]
        def dfs(i,target):
            if target == 0:
                return True
            if i>=n or target<0:
                return False
            if mem[i][target] != -1:
                return mem[i][target]
            mem[i][target] = (dfs(i+1,target) or dfs(i+1,target-nums[i]))
            return mem[i][target]
        return dfs(0,target)