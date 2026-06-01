class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        check = {}
        for ch in s:
            if ch in seen:
                seen[ch] += 1
            else:
                seen[ch] = 1
        for ch in t:
            if ch in check:
                check[ch] += 1
            else:
                check[ch] = 1
        return seen == check