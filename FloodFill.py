"""
https://leetcode.com/problems/flood-fill/description/
733. Flood Fill
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input:
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation:
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
Note:

The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
"""

class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        maxRows = len(image)
        maxCols = len(image[0])
        startCoord = (sr, sc)
        starColor = image[startCoord[0]][startCoord[1]]
        toFlip = [startCoord]
        queue = [startCoord]
        visited = set()
        while queue:
            current = queue.pop(0)
            if current not in visited:
                visited.add(current)
                image[current[0]][current[1]] = newColor
                neighbors = self.get_neighbors(current, maxRows, maxCols)
                sameColorNeighbors = self.filter_by_color(image, neighbors , starColor)
                if sameColorNeighbors:
                    for n in sameColorNeighbors:
                        queue.append(n)
        return image






    def get_neighbors(self, coord: (int, int), maxRows: int, maxCols: int)->[(int, int)]:
        x1,y1 = coord
        result = [(x1-1,y1),(x1+1,y1),(x1,y1-1),(x1,y1+1)]
        return [(x,y) for x, y in result if x >=0 and y >=0 and x < maxRows and y < maxCols ]

    def filter_by_color(self, image: [[int]], candidates: [(int, int)], color: int)-> [(int, int)]:
        return [(x,y) for x, y in candidates if image[x][y] == color]

#
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2
sol = Solution()
sol.floodFill(image, sr, sc, newColor)
for row in image: print(row)
