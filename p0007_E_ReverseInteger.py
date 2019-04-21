# -*- coding: utf-8 -*-
# @Time    : 2017/10/9 18:19
# @Author  : Yulong Liu
# @File    : p0007_E_ReverseInteger.py

"""
题号：7
难度：easy
链接：https://leetcode.com/problems/reverse-integer/description/
描述：输入一个32位有符号数的十进制形式，将其各位数字颠倒后返回（颠倒后越界的话返回0）
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if str(x).startswith('-'):
            flag = '-'
            x = str(x)[1:]
        else:
            flag = ''
            x = str(x)
        y = flag + x[::-1]
        if -2147483648 <= int(y) <= 2147483647:
            return int(y)
        else:
            return 0


if __name__ == '__main__':
    print(Solution().reverse(-2147483641))
    print(Solution().reverse(0))
    print(2**31 - 1)
    print(-2**31)
