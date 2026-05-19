# from collections import Counter
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         if k == len(nums):
#             return nums

#         count = Counter(nums)

#         return heapq.nlargest(k, count.keys(), key=count.get)

    
        

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return nums
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

            #counting all values
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            freq[c].append(n)


        res = []
        for i in range(len(freq) -1, 0 , -1):
            for n in freq[i]:
                res.append(n)

                if len(res) == k: return res



        