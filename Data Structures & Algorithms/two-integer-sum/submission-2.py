class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i, n in enumerate(nums):
            rem = target - n
            if rem in res:
                return [res[rem], i]
            res[n] = i