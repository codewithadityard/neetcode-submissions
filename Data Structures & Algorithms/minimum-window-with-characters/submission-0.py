class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hmap1={}
        hmap2={}
        left=0
        right=0
        res=float("inf")
        length=0
        idx=[-1,-1]

        if t=="":
            return ""


        for st in t:
            hmap1[st]=hmap1.get(st,0)+1

        need=len(hmap1)
        have=0

        while right < len(s):
            hmap2[s[right]]=hmap2.get(s[right],0)+1

            if s[right] in hmap1 and hmap2[s[right]]== hmap1[s[right]]:
                have+=1
    
            
            while have == need:

                length=right-left+1
                if res > length:
                    res=length
                    idx=[left,right]
                
                hmap2[s[left]]-=1

                if s[left] in hmap1 and hmap2[s[left]]<hmap1[s[left]]:
                    have-=1

                left+=1
            right+=1
        
        left,right=idx

    
        return s[left:right+1] if res != float("inf") else ""

            


