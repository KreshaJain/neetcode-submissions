class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.child:
                cur.child[c] = TrieNode()
            cur = cur.child[c]
        cur.end = True
    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.child:
                return False
            cur = cur.child[c]
        return cur.end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.child:
                return False
            cur = cur.child[c]
        return True 
class TrieNode:
    def __init__(self):
        self.child = {}
        self.end = False