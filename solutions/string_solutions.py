from typing import List

# https://leetcode.com/problems/longest-substring-without-repeating-characters/
def lengthOfLongestSubstring(s: str) -> int:
    longest = 0
    for index1, char1 in enumerate(s):
        substring = char1
        if longest == 0:
            longest = 1
        for index2, char2 in enumerate(s[index1+1:]):
            if char2 not in substring:
                substring = substring + char2
                if index2 + 2 > longest:
                    longest = index2 + 2
            else:
                break
            
    return longest

# https://leetcode.com/problems/zigzag-conversion/
def convert(self, s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    stringDict = {x:'' for x in range(numRows)}
    goingDown = True
    index = 0
    for char in s:
        if(goingDown):
            stringDict[index] += char
            if index == numRows - 1:
                goingDown = False
                index -= 1
            else:
                index += 1
        else:
            stringDict[index] += char
            if index == 0:
                goingDown = True
                index += 1
            else:
                index -= 1
    out = ''
    for key in stringDict:
        out = out + stringDict[key]
        
    return out