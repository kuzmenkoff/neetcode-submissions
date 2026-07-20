class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        i = 0
        for i in range(len(nums)):
            if nums[i] > 0:
                break;
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[j] + nums[k] == -nums[i]:
                    if [nums[i], nums[j], nums[k]] not in result:
                        result.append([nums[i], nums[j], nums[k]])
                    k = k - 1
                    j = j + 1
                elif nums[j] + nums[k] > -nums[i]:
                    k = k - 1
                elif nums[j] + nums[k] < -nums[i]:
                    j = j + 1
        return result
        