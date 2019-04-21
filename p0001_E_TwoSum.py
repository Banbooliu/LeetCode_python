# -*- coding: utf-8 -*-
# @Time    : 2017/10/4 23:54
# @Author  : Yulong Liu
# @File    : p0001_E_TwoSum.py

"""
题号：1
难度：easy
链接：https://leetcode.com/problems/two-sum/description/
描述：一个list里正好有两个数相加等于target，找出这两个数的位置
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, x in enumerate(nums):
            for j, y in enumerate(nums[i+1:]):
                if x + y == target:
                    return [i, i+1+j]


if __name__ == '__main__':
    test_list = [2, 7, 11, 15]
    print(Solution().twoSum(test_list, 9))