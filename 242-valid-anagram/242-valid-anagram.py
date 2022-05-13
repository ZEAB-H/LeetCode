class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    
        anagram1 = set(s)
        anagram2 = set(t)
        
        for i in anagram1:
            if anagram1 !=anagram2:
               return False
        return True