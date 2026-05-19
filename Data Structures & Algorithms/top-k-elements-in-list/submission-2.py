class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for i in nums:
            if i not in res:
                res[i] = 1
            else:
                res[i] += 1
        ans = sorted(res, key=lambda x:res[x], reverse=True)
        
        return ans[:k]