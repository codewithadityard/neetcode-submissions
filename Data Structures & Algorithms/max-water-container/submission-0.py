class Solution:
    def maxArea(self, height: list[int]) -> int:
        left=0
        right=len(height)-1
        result=0
        value=0
        while(left<=right):
            if height[left]<height[right]:
                value=(right-left)*height[left]
                left+=1
            elif height[left]>height[right]:
                value=(right-left)*height[right]
                right-=1
            else:
                value=(right-left)*height[left]
                left+=1
                right-=1
            
            result=max(result,value)
    
        return result

        