class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # for r in range(len(matrix)):
        #     for c in range(len(matrix[0])):
        #         if matrix[r][c] == target:
        #             return True
        #     return False


        # m, n = len(matrix), len(matrix[0])
        # r = 0
        # c = n -1

        # while r < m and c >= 0:
        #     if matrix[r][c] > target:
        #         c -= 1
        #     elif matrix[r][c] < target:
        #         r +=1
        #     else:
        #         return True
        # return False



        # rows, cols = len(matrix), len(matrix[0])
        # top, bot = 0, rows-1
        # while top <= bot:
        #     row = (top+bot)//2
        #     if target > matrix[row][-1]:
        #         top = row + 1
        #     elif target < matrix[row][0]:
        #         bot = row - 1

        #     else:
        #         break

        # if not (top <= bot):
        #     return False

        # row = (top + bot) // 2
        # l, r = 0, cols - 1
        # while l <= r:
        #     m = (l + r) //2
        #     if target > matrix[row][m]:
        #         l = m + 1
        #     elif target < matrix[row][m]:
        #         r = m - 1
        #     else:
        #         return True
        # return False

        rows , cols = len(matrix), len(matrix[0])

        l,r = 0, rows * cols -1
        while l <=r:
            m = l + (r -l)//2
            row, col = m // cols, m % cols 

            if target > matrix[row][col]:
                l = m + 1
            elif target < matrix[row][col]:
                r = m - 1
            else:
                return True
        return False