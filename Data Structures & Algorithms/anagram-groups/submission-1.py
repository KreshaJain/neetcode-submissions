class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for word in strs:
            count =[0]*26
            for ch in word:
                id = ord(ch) - ord('a')
                count[id] = count[id]+1
            key = tuple(count)
            if key in d:
                d[key].append(word)
            else:
                d[key] = [word]
        return list(d.values())