# -*- coding: utf-8 -*-
# @Time    : 2017/10/9 18:31
# @Author  : Yulong Liu
# @File    : p0008_M_StringToInteger(atoi).py

"""
题号：8
难度：medium
链接：https://leetcode.com/problems/string-to-integer-atoi/description/
描述：自己实现一个字符串转十进制int的函数，这题很蛋疼，可以不做
"""

INT_MAX = 2147483647
INT_MIN = -2147483648


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        i = 0
        res = 0
        negative = 1
        length = len(str)

        while i < length and str[i] == ' ':
            i += 1

        if i == length:
            return 0

        if str[i] == '+':
            i += 1
        elif str[i] == '-':
            negative = -1
            i += 1

        while i < length and '0' <= str[i] <= '9':
            res = (res * 10) + int(str[i])
            if res > INT_MAX or res < INT_MIN:
                return INT_MAX if negative > 0 else INT_MIN
            i += 1
        return res * negative

if __name__ == '__main__':
    print(Solution().myAtoi('  -12b23d '))
    print(Solution().myAtoi('  '))
    print(Solution().myAtoi(''))
    print(Solution().myAtoi('123'))
    print(Solution().myAtoi('1234567890123'))
