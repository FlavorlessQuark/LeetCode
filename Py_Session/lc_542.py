class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dp = {}
        width = len(mat[0])
        height = len(mat)

        for y in range(height):
            for x in range(width):
                if (mat[y][x] != 0):
                    mat[y][x] = 0x6FFFFFF
                    if (x - 1 >= 0):
                        mat[y][x] = min (mat[y][x] , mat[y][x - 1] + 1)
                    if (y - 1 >= 0):
                        mat[y][x] = min (mat[y][x] , mat[y - 1][x] + 1)

        # print(mat)
        for y in range(height - 1 , -1 , -1):
            for x in range(width -1, -1, -1):
                if (mat[y][x] != 0):
                    if (x + 1 < width):
                        mat[y][x] = min (mat[y][x] , mat[y][x + 1] + 1)
                    if (y + 1 < height):
                        mat[y][x] = min (mat[y][x] , mat[y + 1][x] + 1)
        # print(d)
        return mat
