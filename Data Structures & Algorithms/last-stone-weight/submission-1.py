class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            f = heapq.heappop(stones)
            l = heapq.heappop(stones)
            if l>f:
                heapq.heappush(stones,f-l)
        stones.append(0)
        return abs(stones[0])