"""
https://leetcode.com/problems/unique-morse-code-words/description/
804. Unique Morse Code Words
DescriptionHintsSubmissionsDiscussSolution
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cab" can be written as "-.-.-....-", (which is the concatenation "-.-." + "-..." + ".-"). We'll call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.

Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation:
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".


Note:

The length of words will be at most 100.
Each words[i] will have length in range [1, 12].
words[i] will only consist of lowercase letters.
"""

class Solution:
    def uniqueMorseRepresentations(self, words: [str]):
        """
        :type words: List[str]
        :rtype: int
        """
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
                 "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
                 "..-","...-",".--","-..-","-.--","--.."]
        str = 'abcdefghijklmnopqrstuvwxyz'
        dict = {str[i]:codes[i] for i in range(26)}
        codes = {self.to_morse_code(word, dict) for word in words}
        return len(codes)

    def to_morse_code(self, word: str, dict: {str, str})-> str:
        return "".join([dict[char] for char in word])

# codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
#          "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
#          "..-","...-",".--","-..-","-.--","--.."]
# str = 'abcdefghijklmnopqrstuvwxyz'
# dict = {str[i]:codes[i] for i in range(26)}
# sol = Solution()
# print(sol.to_morse_code("abc", dict))