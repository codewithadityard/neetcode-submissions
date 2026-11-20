class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        right=0
        freq={}
        maxf=0
        result=0

        for right in range(len(s)):
            freq[s[right]]=freq.get(s[right],0)+1
            maxf=max(maxf,freq[s[right]])


            size=right-left+1
            while size-maxf>k:
                freq[s[left]]-=1
                left+=1
                size=right-left+1
                result=max(result,size)
            
            result=max(result,size)
        return result
        


        