class Solution:
    def isPalindrome(self, s: str)->bool:
        string="".join(s.split())
        stg=""
        for st in string:
            if st.isalnum():
                stg+=st.lower()
                

        left=0
        right=len(stg)-1
        while left<right:
            if stg[left]!=stg[right]:
                return False
            left+=1
            right-=1
            
        return True


        