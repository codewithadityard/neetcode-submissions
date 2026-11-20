class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left=0
        right=0
        hmap1={}
        hmap2={}

        if len(s1)>len(s2):
            return False

        for st in s1:
            hmap1[st]=hmap1.get(st,0)+1


        for right in range(len(s1)):
            hmap2[s2[right]]=hmap2.get(s2[right],0)+1

        for right in range(len(s1),len(s2)):
            if hmap1==hmap2:
                return True
            hmap2[s2[right]]=hmap2.get(s2[right],0)+1
            hmap2[s2[left]]-=1
            if hmap2[s2[left]]<=0:
                del hmap2[s2[left]]

            left+=1

        if hmap1==hmap2:
            return True

        return False




        