class WordDictionary:

    def __init__(self):
        self.root = self.TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if node.chars.get(char):
                node = node.chars.get(char)
            else:
                new = self.TrieNode()
                node.chars[char] = new
                node = new
        node.word = True

    def search(self, word: str) -> bool:
        def helper(node, word):
            for i in range(len(word)):
                
                if word[i] == '.':
                    for n in node.chars.values():
                        if helper(n, word[i+1:]):
                            return True
                    return False
                elif word[i] in node.chars:
                    node = node.chars.get(word[i])
                else:
                    return False
            return node.word

        return helper(self.root, word)

    class TrieNode:
        def __init__(self):
            self.chars = {}
            self.word = False
        
