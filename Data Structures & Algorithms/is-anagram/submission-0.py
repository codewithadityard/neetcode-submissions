class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1={}
        freq2={}
        for st in s:
            freq1[st]=freq1.get(st,0)+1
        for rt in t:
            freq2[rt]=freq2.get(rt,0)+1

        if freq1==freq2:
            return True
        return False

            

        