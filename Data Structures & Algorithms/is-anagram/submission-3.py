class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charCount = {}
        if(len(s)!= len(t)):
            return False
        for c in s:
            if (c in charCount):
                charCount[c] +=1
            else:
                charCount[c] = 1
        for c in t:
            if (c in charCount):
                charCount[c] -=1
        for count in charCount:
            if(charCount[count] != 0):
                return False
        return True       