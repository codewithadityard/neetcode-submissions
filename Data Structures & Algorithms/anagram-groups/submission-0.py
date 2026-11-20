class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap={}
        anagrams=[]
        for st in strs:
            s="".join(sorted(st))
            if s in hmap:
                hmap[s].append(st)
            else:
                hmap[s]=[st]

        return list(hmap.values())


