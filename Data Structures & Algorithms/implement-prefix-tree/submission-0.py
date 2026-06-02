class PrefixTree:
    
    def __init__(self):
        self.root = self.PrefixTreeNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if node.chars.get(char):
                node = node.chars.get(char)
            else: 
                new = self.PrefixTreeNode()
                node.chars[char] = new
                node = new
        node.word = True
    

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if node: node = node.chars.get(char)
        if node:
            return node.word
        return False

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if node: node = node.chars.get(char)
        return node != None

    class PrefixTreeNode:
        def __init__(self):
            self.chars = {}
            self.word = False
        
        