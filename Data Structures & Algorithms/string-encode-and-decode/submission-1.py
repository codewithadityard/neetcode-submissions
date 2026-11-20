class Solution:

    def encode(self, strs: List[str]) -> str:
        encoder=""
        for st in strs:
            length=str(len(st))
            encoder+=length+"#"+st
            
        return encoder
        

            
    def decode(self, s:str) -> List[str]:
        digits=""
        num=0
        idx=0
        i=0
        decoded=""
        decoded_str=[]
        
        while i < len(s):
            while s[i].isdigit():
                digits+=s[i]
                i=i+1
            num=int(digits)
            digits=""

            if s[i]=="#":
                decoded=s[i+1:i+num+1]
                decoded_str.append(decoded)
                i=i+num+1
        
        return decoded_str


            
            






        return decoded_str


        