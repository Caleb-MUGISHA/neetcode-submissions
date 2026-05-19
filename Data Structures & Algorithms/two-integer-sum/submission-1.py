class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            reminder = target - num
            if reminder in seen:
                return [seen[reminder], i]
            seen[num] = i
