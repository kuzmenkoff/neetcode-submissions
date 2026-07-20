class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while (l < r):
            while numbers[l] + numbers[r] >= target:
                if numbers[l] + numbers[r] == target:
                    return [l + 1, r + 1]
                r = r - 1
            l = l + 1
        return [l + 1, r + 1] 
        