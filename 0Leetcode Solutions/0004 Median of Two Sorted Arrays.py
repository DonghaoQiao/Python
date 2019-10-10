'''
https://leetcode.com/problems/median-of-two-sorted-arrays/
4. Median of Two Sorted Arrays
Hard

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1)==len(nums2)==0:
            return None
        l=len(nums1)+len(nums2)
        if l%2==1:
            return self.findK(nums1,nums2,l//2)
        else:
            return (self.findK(nums1,nums2,l//2-1)+self.findK(nums1,nums2,l//2))/2
    def findK(self,nums1,nums2,k):
        if not nums1: return nums2[k]
        if not nums2: return nums1[k]
        nums1_i,nums2_i=len(nums1)//2,len(nums2)//2
        if nums1_i+nums2_i<k:
            if nums1[nums1_i]>nums2[nums2_i]:
                return self.findK(nums1,nums2[nums2_i+1:],k-nums2_i-1)
            else:
                return self.findK(nums1[nums1_i+1:],nums2,k-nums1_i-1)
        else:
            if nums1[nums1_i]>nums2[nums2_i]:
                return self.findK(nums1[:nums1_i],nums2,k)
            else:
                return self.findK(nums1,nums2[:nums2_i],k)

class Solution1(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1)==len(nums2)==0:
            return None
        len1,len2=len(nums1),len(nums2)
        l=len1+len2
        if l%2==1:
            return self.findK(nums1,nums2,l//2+1)
        else:
            return (self.findK(nums1,nums2,l//2)+self.findK(nums1,nums2,l//2+1))/2
    def findK(self,nums1,nums2,k):
        len1,len2=len(nums1),len(nums2)
        if len1>len2:
            return self.findK(nums2,nums1,k)
        if len1==0:
            return nums2[k-1]
        if k==1:
            return min(nums1[0],nums2[0])
        pa=min(k//2,len1)
        pb=k-pa
        if nums1[pa-1]<=nums2[pb-1]:
            return self.findK(nums1[pa:],nums2,pb)
        else:
            return self.findK(nums1,nums2[pb:],pa)


print(Solution().findMedianSortedArrays([],[]))
print(Solution().findMedianSortedArrays([6,7],[]))
print(Solution().findMedianSortedArrays([2],[1,3]))
print(Solution().findMedianSortedArrays([1,3],[2]))
print(Solution().findMedianSortedArrays([1,2],[3,4]))
print(Solution().findMedianSortedArrays([1],[3,4,5,6]))
