class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        #for i in piles:
         #   k.append(i//c++)
        
        l,r=1,max(piles)
        ans = r
        while l<=r:
            m = (l+r)//2
            hours=0
            for p in piles:
                hours+=(p+m-1)//m
            if hours<=h:
                ans = m
                r=m-1
            else:
                l=m+1
        return ans