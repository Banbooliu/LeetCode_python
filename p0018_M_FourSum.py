# -*- coding: utf-8 -*-
# @Time    : 2019/5/3 10:01
# @Author  : Yulong Liu
# @File    : p0018_M_FourSum.py


"""
题号：18
难度：medium
链接：https://leetcode.com/problems/4sum/
描述：3sum 的升级，一串数字中，找出和为 target 的所有组合
"""

from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """2sum 和 3sum 的再升级
        我想用 n 倍的 3sum 来解决
        """

        def threeSum(nums: List[int], target, x: int, low: int):
            """
            从 nums[low] 到 nums[-1] 之间，
            找到和为 target 的所有不重复的 三元数组
            然后与 x 一起加入 res 中
            把值都传进来的目的是，避免重新分配空间
            """
            if 3 * nums[low] > target:
                return None

            for i in range(low, len(nums) - 2):
                if i > low and nums[i] == nums[i - 1]:
                    continue
                l, r = i + 1, len(nums) - 1
                while l < r:
                    s = nums[i] + nums[l] + nums[r]
                    if s < target:
                        l += 1
                    elif s > target:
                        r -= 1
                    else:
                        res.append([x, nums[i], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1

        if not nums or len(nums) < 4:
            return []

        nums.sort()
        if 4 * nums[0] > target or 4 * nums[-1] < target:
            return []

        res = []
        length = len(nums)
        for i in range(length - 1):
            x = nums[i]
            if i and x == nums[i - 1]:
                continue
            if x + 3 * nums[-1] < target:
                continue
            if x * 4 > target:
                break
            if x * 4 == target:
                if i + 3 < length and nums[i + 3] == x:
                    res.append([x, x, x, x])
                    continue

            threeSum(nums, target - x, x, i + 1)
        return res

    def fourSum_TODO(self, nums: List[int], target: int) -> List[List[int]]:
        """看了 discuss，有人干脆设计了 nSum 算法，其中包括了 2sum 和 3sum"""


if __name__ == '__main__':
    data = [1, 4, -3, 0, 0, 0, 5, 0]
    target = 0
    print(Solution().fourSum(data, target))
