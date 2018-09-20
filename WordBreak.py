"""
https://leetcode.com/problems/word-break/description/
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

"""
from Tries.PrefixTrie import TrieNode
class WordBreak1:

    def get_starting_words(self, input: str, trie: TrieNode) -> [(str, str)]:
        results = []
        currentWord = ''
        while input:
            top , input = input[0], input[1:]
            currentWord+=top
            if trie.contains_prefix(currentWord):
                if trie.contains_word(currentWord):
                    results.append((currentWord , input))
            else: return results
        return results

    def word_split(self, word: str, trie: TrieNode):
        results = []
        queue = self.get_starting_words(word, trie)
        while queue:
            start, remain = queue.pop()
            if not remain: results.append(start)
            else:
                for st, rm in self.get_starting_words(remain, trie): queue.append((start +' '+ st, rm))
        return results

    def word_break(self, s, worddict):
        trie = TrieNode()
        for word in worddict : trie.insert_word(word)
        queue = self.get_starting_words(word, trie)
        while queue:
            start, remain = queue.pop()
            if not remain: return True
            else: return self.word_break(remain, worddict)







#
wordDict = ["aditya", "goyal", "working", "python", "blah", 'blahh' ,'h']
trie = TrieNode()
for word in wordDict: trie.insert_word(word)

input = 'adityagoyalblahh'
# starts = wb.get_starting_words(input)
# print(starts)

# wsplit = wb.word_split('aditad')
# print(wsplit)
wb = WordBreak1()
print(wb.word_split(input, trie))