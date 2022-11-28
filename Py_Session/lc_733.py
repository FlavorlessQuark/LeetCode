class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        oc = image[sr][sc]

        if (oc == color):
            return image
        def recurse(x, y):
            if (image[x][y] == oc):
                image[x][y] = color
                if (x - 1 >= 0):
                    recurse(x - 1, y)
                if (x + 1 < len(image)):
                    recurse(x + 1, y)
                if (y - 1 >= 0):
                    recurse(x, y - 1)
                if (y + 1 < len(image[0])):
                    recurse(x, y + 1)
        recurse(sr, sc)
        return image
