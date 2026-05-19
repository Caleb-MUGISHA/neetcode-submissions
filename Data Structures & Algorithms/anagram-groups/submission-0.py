class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for i in strs:
            sorted_st= "".join(sorted(i))

            if sorted_st not in hashmap:
                hashmap[sorted_st] = [i]
            else:
                hashmap[sorted_st].append(i)

        return list(hashmap.values())



        

 

            