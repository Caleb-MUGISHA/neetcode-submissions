class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for idx, val in enumerate(nums):
            rem = target - val
            if rem in d:
                return [d[rem], idx]
            d[val] = idx

        return None
            

        