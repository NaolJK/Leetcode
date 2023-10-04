class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    
    def __init__(self):
        
        self.root = TrieNode()
    
    def insert(self, string:str):
        
        cur = self.root
        
        for c in string:
            
            if c not in cur.children:
                
                cur.children[c] = TrieNode()
        
            cur = cur.children[c]
            
        cur.isEnd = True
    
    def search(self, string:str):
        
        cur = self.root
        
        def dfs(i, node):
            
            if i >= len(string) and node.isEnd:
                return True
            
            if i >= len(string):
                # print(node.children.keys(), i, string)
                return False
            
           
            
            
            if string[i] == '.':
                for key, val in node.children.items():
                      if dfs(i+1, val):
                            return True
                return False
            else:
                if string[i] in node.children:
                    return dfs(i+1, node.children[string[i]])
                else:
                    return False
                    
        return dfs(0, cur)
            
        

class WordDictionary:

    def __init__(self):
        self.trie = Trie()
        

    def addWord(self, word: str) -> None:
        self.trie.insert(word)
        

    def search(self, word: str) -> bool:
        return self.trie.search(word)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)