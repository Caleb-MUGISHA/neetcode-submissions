class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            x, y = stones[-2], stones[-1]
            if x == y:
                stones = stones[:-2]
            else:
                stones = stones[:-2] + [y - x]
        return stones[0] if stones else 0