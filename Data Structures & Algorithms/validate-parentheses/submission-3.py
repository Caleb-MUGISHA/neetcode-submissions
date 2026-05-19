class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False
        parant = {'(':')', '{': '}', '[':']'}
        stack = []
        for i in s:
            if i in parant:
                stack.append(i)
            elif len(stack) == 0 or parant[stack.pop()] != i:   return False

        return len(stack) == 0
        
        