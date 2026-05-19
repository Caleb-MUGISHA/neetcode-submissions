class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # while len(stones) > 1:
        #     stones.sort()
        #     x, y = stones[-2], stones[-1]
        #     if x == y:
        #         stones = stones[:-2]
        #     else:
        #         stones = stones[:-2] + [y - x]
        # return stones[0] if stones else 0

        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if first < second:
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])