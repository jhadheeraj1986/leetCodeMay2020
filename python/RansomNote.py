'''
Given an arbitrary ransom note string and another string containing letters from all the magazines, 
write a function that will return true if the ransom note can be constructed from the magazines ; 
otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if (ransomNote == ""):
            return  True
        
        ransomNoteDict = dict()
        magazineDict = dict()
        flag = False
        for letter in ransomNote:
            if letter in ransomNoteDict:
                ransomNoteDict[letter] = ransomNoteDict[letter] + 1
            else:
                ransomNoteDict[letter] = 1
                
        for letter in magazine:
            if letter in magazineDict:
                magazineDict[letter] = magazineDict[letter] + 1
            else:
                magazineDict[letter] = 1
            
        for item in ransomNoteDict:
            if (item in magazineDict) and (ransomNoteDict[item] <= magazineDict[item]):
                flag = True
            else:
                flag = False
                return flag
        
        
        # print(ransomNoteDict)
        # print(magazineDict)
        return flag
