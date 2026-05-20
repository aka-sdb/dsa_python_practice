"""
Brute Force solution - 2 nested loops
Outer loop is looping through all the words present in the list.
We actually take out the first word and loop through the remaining words.
This is done because we need a point of comparison.

If the string is empty or the first characters of both the words do not match, simply exit.
If the first characters match, then we take the minimum lengths of the 2 words, and start character comparison.

There is a possibility that the length of the common prefix between first 2 words is more than the 1st and 3rd word.
In this case, we must consider the shorter prefix because that is the common prefix among the 3 words.
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]
        num_words = len(strs)
        if num_words == 1:
            return first
    
        if len(first) == 0:
            return ""
    
        res = ""

        for i in range(1, num_words):
            word = strs[i]
            if (len(word) == 0) or (first[0] != word[0]):
                return ""
            
            else:
                m = len(first)
                p = len(word)
                pref = ""
                upper_lmt = min(m, p)

                for j in range(0, upper_lmt):
                    if first[j] != word[j]:
                        break
                    else:
                        pref = pref + "" + first[j]

                if len(res) == 0:
                    res = pref
                elif len(pref) < len(res):
                    res = pref

        return res   