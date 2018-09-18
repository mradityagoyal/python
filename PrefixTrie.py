class TreeNode(object):
    def __init__(self):
        self.dict = {}

    def insert(self, word):
        first_char = word[0]
        if first_char in self.dict:
            self.dict[first_char].insert(word[1::])
        else: self.dict[first_char] = TreeNode()
