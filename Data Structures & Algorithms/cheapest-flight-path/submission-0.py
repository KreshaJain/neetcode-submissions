class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        pr = [float("inf")]*n
        pr[src]=0
        for i in range(k+1):
            temppr = pr.copy()
            for s,d,p in flights:
                if pr[s] == float("inf"):
                    continue
                if pr[s]+p<temppr[d]:
                    temppr[d] = pr[s]+p
            pr = temppr
        if pr[dst] == float("inf"):
            return -1
        else:
            return pr[dst]