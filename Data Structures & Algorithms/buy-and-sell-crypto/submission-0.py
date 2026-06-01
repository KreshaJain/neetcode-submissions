class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp=0
        minb=prices[0]
        for i in prices:
            maxp=max(maxp,i-minb)
            minb=min(minb,i)
        return maxp
        