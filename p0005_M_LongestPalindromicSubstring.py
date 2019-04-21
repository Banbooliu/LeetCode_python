# -*- coding: utf-8 -*-
# @Time    : 2017/10/5 15:43
# @Author  : Yulong Liu
# @File    : p0005_M_LongestPalindromicSubstring.py

"""
题号：5
难度：medium
链接：https://leetcode.com/problems/longest-palindromic-substring/description/
描述：找出一个长度不大于1000的字符串中的最长回文子串（非子序列）
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        思路：dp
        :type s: str
        :rtype: str
        """
        if not s:
            return ''

        size = len(s)
        start = 0
        max_length = 1
        F = [[False for x in range(size)] for y in range(size)]
        # 初始化边界数据
        for i in range(size):
            F[i][i] = True
            if i+1 < size and s[i] == s[i+1]:
                F[i][i+1] = True
                start = i
                max_length = 2

        # 依次判断每个长度的子串（由于长度1和2已结初始化了，这里直接从3开始判断）
        for length in range(3, size+1):
            for i in range(size-length+1):
                j = i + length - 1
                if F[i+1][j-1] and s[i] == s[j]:
                    F[i][j] = F[i+1][j-1]
                    if length > max_length:
                        start = i
                        max_length = length
        return s[start:start+max_length]

    def longestPalindrome2(self, s):
        """
        从网上抄的代码，效率超高
        :type s: str
        :rtype: str
        """
        ls = len(s)
        maxs = ''
        i = 0
        while 2 * (ls - i) - 1 > len(maxs):
            pl = pr = i
            # move the current index (i) and the right pointer (pr), if the consecutive letters are the same
            while pr < ls - 1 and s[pr] == s[pr + 1]:
                i += 1
                pr += 1

            # move left and right pointers, so that the substring between them is longer than maxs
            dif = len(maxs) - (pr - pl)
            if dif > 0:
                dif += dif % 2
                pl, pr = pl - dif / 2, pr + dif / 2

            # check whether the substring is palindrome.
            # If yes, try to further extend it, and then replace maxs with the new substring
            if s[pl:pr + 1] == s[pr:(pl - 1 if pl > 0 else None):-1]:
                while pl > 0 and pr < ls - 1 and s[pl - 1] == s[pr + 1]:
                    pl -= 1
                    pr += 1
                maxs = s[pl:pr + 1]
            i += 1
        return maxs

if __name__ == '__main__':
    print(Solution().longestPalindrome('babad'))