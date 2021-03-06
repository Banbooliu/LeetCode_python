# -*- coding: utf-8 -*-
# @Time    : 2019/3/24 17:28
# @Author  : Yulong Liu
# @File    : p0011_M_ContainerWithMostWater.py

"""
题号：11
难度：medium
链接：https://leetcode.com/problems/container-with-most-water
描述：等距柱形图哪两根柱子之间装水更多
"""

from typing import List


class Solution(object):
    def maxArea01(self, height: List[int]) -> int:
        """先撸一个暴力的"""
        max_area = 0
        for i, a1 in enumerate(height):
            for j, a2 in enumerate(height[i + 1:]):
                max_area = max(max_area, min(a1, a2) * (j + 1))
        return max_area

    def maxArea02(self, height: List[int]) -> int:
        """从左右往中间压缩。由于总面积是较短的一根决定的
        考虑到，如果 height[left] < height[right]
        那么即使 right -= 1，max_area 也不会超过当前面积，
        反而 left += 1，面积还有可能更大，因此此时应 left += 1
        另一个方向的判断同理
        """
        max_area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            if height[left] < height[right]:
                max_area = max(max_area, height[left] * (right - left))
                left += 1
            else:
                max_area = max(max_area, height[right] * (right - left))
                right -= 1
        return max_area


if __name__ == '__main__':
    data = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(Solution().maxArea02(data))
