class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []

        for temp in range(len(nums) - 2):

            # Skip duplicate fixed elements
            if temp > 0 and nums[temp] == nums[temp - 1]:
                continue

            left = temp + 1
            right = len(nums) - 1

            while left < right:

                total = nums[temp] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[temp], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # Skip duplicate left values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate right values
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total > 0:
                    right -= 1

                else:
                    left += 1

        return result
        