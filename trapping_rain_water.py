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
        reverse = height.reverse()
