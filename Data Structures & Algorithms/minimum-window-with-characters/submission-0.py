class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        count = {}
        win = {}
        
        for i in t:
            count[i] = 1 + count.get(i,0)
        have = 0
        need=len(count)
        res = [-1,-1]
        reslen=float("infinity")
        l=0
        for r in range(len(s)):
            win[s[r]] = 1 + win.get(s[r],0)
            if s[r] in count and win[s[r]] == count[s[r]]:
                have += 1
            while have == need:
                if(r-l+1) < reslen:
                    res = [l,r]
                    reslen = (r-l+1)
                win[s[l]] -= 1

                if s[l] in count and win[s[l]] < count[s[l]]:
                    have -= 1

                l+=1
        l,r = res
        if reslen!=float("infinity"):
            return s[l:r+1]
        else:
            return ""
            