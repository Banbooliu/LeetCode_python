# -*- coding: utf-8 -*-
# @Time    : 2019/4/14 23:43
# @Author  : Yulong Liu
# @File    : p0014-LongestCommonPrefix.py


"""
题号：14
难度：easy
链接：https://leetcode.com/problems/longest-common-prefix
描述：多个字符串找公共子串(a-z)
"""

from typing import List


class Solution:
    def longestCommonPrefix2(self, strs: List[str]) -> str:
        """简单粗暴的方式"""
        res = ''
        if not strs:
            return res
        for char in zip(*strs):
            if len(set(char)) == 1:
                res += char[0]
            else:
                return res
        return res

    def longestCommonPrefix(self, strs: List[str]) -> str:
        """不需要一个一个字符地加，只需要找到分界点，一次性取出即可"""
        if not strs:
            return ''
        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)


if __name__ == '__main__':
    a = ["flower","flow","flight"]
    res = Solution().longestCommonPrefix(a)
    print(res)