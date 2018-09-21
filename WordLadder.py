"""
https://leetcode.com/problems/word-ladder/description/
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""

class WordLadder:

    def ladderLength(self, beginWord : str, endWord: str, wordList: [str]) -> int:
        wordList = set(wordList)
        queue = []
        queue.append((beginWord, 1))
        visited = set()
        while queue:
            currentWord, currPathLen = queue.pop(0)
            if currentWord == endWord : return currPathLen
            if currentWord not in visited:
                visited.add(currentWord)
                wordList.discard(currentWord)
                neighbors = {word
                             for word in wordList
                                if word not in visited
                                and self.is_one_char_away(word, currentWord)
                             }
                if endWord in neighbors: return currPathLen + 1
                queue += [(n, currPathLen+1) for n in neighbors]
        return 0


    def is_one_char_away(self, s1: str, s2: str) -> bool:
        return len([ x for x, y in zip(s1, s2) if x != y]) == 1

#
#one workd away
wl = WordLadder()

s1 = "hot"
s2 = "hit"
print('"%s" is one char away from "%s" : %s' %(s1 , s2, wl.is_one_char_away(s1,s2)))

s2 = 'pit'
print('"%s" is one char away from "%s" : %s' %(s1 , s2, wl.is_one_char_away(s1,s2)))

s2 = 'pot'
print('"%s" is one char away from "%s" : %s' %(s1 , s2, wl.is_one_char_away(s1,s2)))

wordList = ["hot","dot","dog","lot","log","cog"]
s1= 'hit'
s2 = 'cog'

print(wl.ladderLength(s1,s2, wordList))