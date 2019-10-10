'''
https://leetcode.com/problems/trapping-rain-water/
42. Trapping Rain Water
Hard

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        result=0
        left,right=0,len(height)-1
        leftWall=rightWall=float('-inf')
        while left<=right:
            if leftWall<=rightWall:
                result+=max(0,leftWall-height[left])
                leftWall=max(leftWall,height[left])
                left+=1
            else:
                result+=max(0,rightWall-height[right])
                rightWall=max(rightWall,height[right])
                right-=1
        return result

print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(Solution().trap([1,2,1,3]))