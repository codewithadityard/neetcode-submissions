class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        result=[]
        zeros=[0]*len(nums)
        count=0
        for num in nums:
            if num ==0:
                count+=1
            else:
                product*=num

        if count > 1:
            return zeros
        else:
            for i in range(len(nums)):
                if nums[i]==0:
                    zeros[i]=product
                    return zeros


        for p in nums:
            if p == 0:
                p=1
            r=int(product/p)
            result.append(r)


        return result

        