class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        count = {}
        win = {}
        for i in s1:
            count[i] = 1 + count.get(i,0)
        l=0
        for r in range(len(s2)):
            win[s2[r]] = 1 + win.get(s2[r],0)
            while r-l+1 > len(s1):
                win[s2[l]] -= 1
                if win[s2[l]] == 0:
                    del win[s2[l]]
                l+=1
            if win==count:
                return True
        return False         