class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for i in strs:
            sorted_st = "".join(sorted(i))

            if sorted_st not in res:
                res[sorted_st] = [i]
            else:
                res[sorted_st].append(i)
        return list(res.values())


        