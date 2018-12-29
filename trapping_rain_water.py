"""
    Key to this problem is to scan the array from left and right side till the longest wall
    Find out what to do with extras
"""

class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        original = [x for x in height]
        height.reverse()
        reverse = height
        print(original, reverse)


Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])