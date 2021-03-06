#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#
# https://leetcode.com/problems/flood-fill/description/
#
# algorithms
# Easy (58.22%)
# Likes:    4015
# Dislikes: 382
# Total Accepted:    402.1K
# Total Submissions: 690.5K
# Testcase Example:  '[[1,1,1],[1,1,0],[1,0,1]]\n1\n1\n2'
#
# An image is represented by an m x n integer grid image where image[i][j]
# represents the pixel value of the image.
#
# You are also given three integers sr, sc, and newColor. You should perform a
# flood fill on the image starting from the pixel image[sr][sc].
#
# To perform a flood fill, consider the starting pixel, plus any pixels
# connected 4-directionally to the starting pixel of the same color as the
# starting pixel, plus any pixels connected 4-directionally to those pixels
# (also with the same color), and so on. Replace the color of all of the
# aforementioned pixels with newColor.
#
# Return the modified image after performing the flood fill.
#
#
# Example 1:
#
#
# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation: From the center of the image with position (sr, sc) = (1, 1)
# (i.e., the red pixel), all pixels connected by a path of the same color as
# the starting pixel (i.e., the blue pixels) are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally
# connected to the starting pixel.
#
#
# Example 2:
#
#
# Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
# Output: [[2,2,2],[2,2,2]]
#
#
#
# Constraints:
#
#
# m == image.length
# n == image[i].length
# 1 <= m, n <= 50
# 0 <= image[i][j], newColor < 2^16
# 0 <= sr < m
# 0 <= sc < n
#
#
#

# @lc code=start
from tracemalloc import start


class Solution:
    # image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    # sr = 1, sc = 1, newColor = 2

    def floodFill(self, image, sr, sc, newColor):
        R = len(image)  # row length
        C = len(image[0])  # column length
        startColor = image[sr][sc]

        if startColor == newColor:
            return image

        def flipColor(row, col):
            if image[row][col] == startColor:
                image[row][col] = newColor
                if row-1 >= 0:
                    flipColor(row-1, col)
                if row+1 != R:
                    flipColor(row+1, col)
                if col-1 >= 0:
                    flipColor(row, col-1)
                if col+1 != C:
                    flipColor(row, col+1)

        flipColor(sr, sc)
        return image

# @lc code=end
