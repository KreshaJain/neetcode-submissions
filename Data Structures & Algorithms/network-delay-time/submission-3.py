class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        ed = collections.defaultdict(list)
        for u,v,t in times:
            ed[u].append((v,t))
        minHeap = [(0,k)]
        visit = set()
        t=0
        while minHeap:
            w,n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = max(t,w)
            for neigh,neighw in ed[n1]:
                if neigh not in visit:
                    heapq.heappush(minHeap,(w + neighw,neigh))
        if len(visit) == n:
            return t
        else:
            return -1