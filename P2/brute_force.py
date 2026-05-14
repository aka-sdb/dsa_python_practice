"""
Brute force solution - 2 nested loops
First, need to find out the length of the longest word.
Then, example WE ARE FINE, need to visualize as
W E
A R E
F I N E

While, no. of words are 3, but FINE is the longest word having length 4
So, outer loop should be driven by the length and inner loop by the word position
as, we need to fix the position of the character and go through every word.
"""

class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        word_count = len(words)
        result = []

        max_len = -1
        for i in words:
            if len(i) > max_len:
                max_len = len(i)

        for j in range(0, max_len):
            new_word = ""
            for k in range(0, word_count):
                n = len(words[k])
                if j > n - 1:
                    new_word = new_word + " "
                else:
                    new_word = new_word + "" + words[k][j]

            result.append(new_word.rstrip())

        return result