# -*- coding: utf-8 -*-
# @Time    : 2017/10/4 23:54
# @Author  : Yulong Liu
# @File    : TwoSum.py


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
    print Solution().twoSum(test_list, 9)