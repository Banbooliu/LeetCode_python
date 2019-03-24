# -*- coding: utf-8 -*-
# @Time    : 2017/10/9 15:36
# @Author  : Yulong Liu
# @File    : ZigZagConversion.py

"""
题号：6
难度：medium
链接：https://leetcode.com/problems/zigzag-conversion/description/
描述：把一串字符按照竖着的Z字形排列，并且横着读出来，具体要看例子才懂
"""

from itertools import zip_longest


class Solution(object):
    def convert(self, s, numRows):
        """
        自己写的方法
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        step = (numRows-1) * 2
        # step = [(x-1)*2 for x in xrange(1, numRows+1)]
        m = [''] * step

        # 拆分字符串
        for index, x in enumerate(s):
            m[index % step] += x

        # 按新逻辑拼接
        res = m[0]
        for i in range(1, numRows-1):
            for x, y in zip_longest(m[i], m[step-i]):
                res += x
                if y:
                    res += y
        res += m[numRows-1]
        return res

    def convert2(self, s, numRows):
        """
        抄的，这思路真简洁
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            # print L
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        return ''.join(L)

if __name__ == '__main__':
    # print(Solution().convert2('ABCDEFGHIJKLMNOPQRST', 4))
    print(Solution().convert('abcdefghijklmn', 4))
    # print(Solution().convert('', 1))
