class Solution:
    def getAnagramPattern(self, s: str):
        return tuple(sorted(s))
        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramsDict = {}
        for s in strs:
            anagram_pattern = self.getAnagramPattern(s)
            if anagram_pattern in anagramsDict:
                anagramsDict[anagram_pattern].append(s)
            else:
                anagramsDict[anagram_pattern] = [s]
        return list(anagramsDict.values())

        