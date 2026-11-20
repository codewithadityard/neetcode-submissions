class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap={}
        result=[]
        for i in range(len(nums)):
            diffrence=target-nums[i]
            if diffrence in hmap:
                return [hmap[diffrence],i]
            else:
                hmap[nums[i]]=i

        return result


