# -*- coding: utf-8 -*-
# @Time    : 2017/10/10 16:56
# @Author  : Yulong Liu
# @File    : p0009-PalindromeNumber.py

"""
题号：9
难度：easy
链接：https://leetcode.com/problems/palindrome-number/description/
描述：判断一个int是不是回文数，要求不使用额外空间（出题人是sb）
"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        y = 0
        while y < x:
            y = y * 10 + x % 10
            x /= 10
        if x == y or x == y / 10:
            return True
        else:
            return False

    def isPalindrome2(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        y = x[::-1]
        return x == y

if __name__ == '__main__':
    print(Solution().isPalindrome(-101))