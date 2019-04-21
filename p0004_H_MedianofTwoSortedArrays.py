# -*- coding: utf-8 -*-
# @Time    : 2017/10/5 12:05
# @Author  : Yulong Liu
# @File    : p0004_H_MedianofTwoSortedArrays.py

"""
题号：4
难度：hard
链接：https://leetcode.com/problems/median-of-two-sorted-arrays/description/
描述：给两个升序排好的整数数组，找出其中位数，要求时间复杂度 O(log (m+n))
"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        思路：每次从两个list里拿出最小的一个，直到找到最中间的一个
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = (len(nums1) + len(nums2)) / 2
        n = 0
        if (len(nums1) + len(nums2)) % 2 == 0:
            n = 1
        else:
            m += 1
        print('m=%d, n=%d' % (m, n))

        while nums1 or nums2:
            x = self.get_next_min(nums1, nums2)
            m -= 1
            if not m:
                if not n:
                    return x
                else:
                    return float(x+self.get_next_min(nums1, nums2)) / 2

    def get_next_min(self, nums1, nums2):
        if not nums1 and not nums2:
            return None
        elif nums1 and not nums2:
            return nums1.pop(0)
        elif nums2 and not nums1:
            return nums2.pop(0)
        else:
            if nums1[0] <= nums2[0]:
                return nums1.pop(0)
            else:
                return nums2.pop(0)

    def findMedianSortedArrays2(self, nums1, nums2):
        """
        思路：从两头往中间走，还没具体看
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        pass

if __name__ == '__main__':
    # a = [1]
    # b = [2, 3]

    # a = [3]
    # b = [1, 2]

    a = [1, 2, 2]
    b = [1, 2, 3]

    # a = [1]
    # b = [2, 3, 4]

    # a = []
    # b = [1]
    print(Solution().findMedianSortedArrays(a, b))
