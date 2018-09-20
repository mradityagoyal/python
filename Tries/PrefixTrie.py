class TrieNode:

    def __init__(self):
        self.children = {}
        self.isWordEnd = False

    def insert_word(self, word: str) -> None:
        current = self
        while word:
            top , word  = word[0], word[1:]
            if top in current.children:
                current = current.children[top]
            else:
                newNode = TrieNode()
                current.children[top] = newNode
                current= newNode
        current.isWordEnd = True

    def contains_prefix(self, prefix: str) -> bool:
        return self.__find_till_end(prefix) is not None

    def contains_word(self, word: str) -> bool:
        last = self.__find_till_end(word)
        return last is not None and last.isWordEnd

    def __find_till_end(self, prefix:str) -> 'TrieNode':
        current = self
        while prefix and current:
            top , prefix  = prefix[0], prefix[1:]
            if top in current.children:
                current = current.children[top]
            else: current = None
        return current

#
# input  = ["aditya", "goyal", "working", "python", "blah", 'blahh']
#
# root = TrieNode()
#
# for word in input: root.insert_word(word)
#
# for word in input: print('%s prefix is contained in Trie : %r' %(word, root.contains_prefix(word)))
#
# for word in input: print('%s WORD is contained in Trie : %r' %(word, root.contains_word(word)))
#
# print('%s WORD is contained in Trie : %r' %('aditaa', root.contains_word('aditaa')))

# print(root.contains_word('ad'))
# print(root.contains_word('adi'))
# print(root.contains_word('aditya'))



