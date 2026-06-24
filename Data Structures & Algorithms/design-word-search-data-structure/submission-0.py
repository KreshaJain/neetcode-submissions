class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.child:
                cur.child[c] = TrieNode()
            cur = cur.child[c]
        cur.end = True

    def search(self, word: str) -> bool:
        def dfs(k,root):
            cur = root
            for i in range(k,len(word)):
                c = word[i]
                if c == ".":
                    for j in cur.child.values():
                        if dfs(i+1,j):
                            return True
                    return False
                else:
                    if c not in cur.child:
                        return False
                    cur = cur.child[c]
            return cur.end
        return dfs(0,self.root)   
class TrieNode:
    def __init__(self):
        self.child = {}
        self.end = False
