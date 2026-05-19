class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplic = set(nums)
        if len(nums) > len(duplic):
            return True
        else: return False
