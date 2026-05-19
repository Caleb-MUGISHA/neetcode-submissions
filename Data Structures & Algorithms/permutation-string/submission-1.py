class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # #Brute force
        # s1 = sorted(s1)

        # for i in range(len(s2)):
        #     for j in range(i, len(s2)):
        #         subStr = s2[i: j+1]
        #         subStr = sorted(subStr)
        #         if subStr == s1: return True
        # return False


        # #hashtable
        # count1 = {}
        # for c in s1:
        #     count1[c] = 1 + count1.get(c, 0)

        
        # need = len(count1)
        # for i in range(len(s2)):
        #     count2, cur = {}, 0
        #     for j in range(i, len(s2)):
        #         count2[s2[j]] = 1 + count2.get(s2[j], 0) 
        #         if count1.get(s2[j], 0) < count2[s2[j]]:
        #             break
        #         if count1.get(s2[j], 0) == count2[s2[j]]:
        #             cur += 1
        #         if cur == need:
        #             return True
        # return False


        if len(s1) > len(s2):
            return False

        s1_count, s2_count = {}, {}

        for i in range(len(s1)):
            s1_count[s1[i]] = 1 + s1_count.get(s1[i], 0)
            s2_count[s2[i]] = 1 + s2_count.get(s2[i], 0)

        if s1_count == s2_count:
            return True

        
        left = 0
        for right in range(len(s1), len(s2)):
            s2_count[s2[right]] = 1 + s2_count.get(s2[right], 0)
            s2_count[s2[left]] -= 1

            if s2_count[s2[left]] == 0:
                del s2_count[s2[left]]


            left += 1


            if s1_count == s2_count:
                return True



        return False
         