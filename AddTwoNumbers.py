# -*- coding: utf-8 -*-
# @Time    : 2017/10/5 00:08
# @Author  : Yulong Liu
# @File    : AddTwoNumbers.py

"""
题号：2
难度：medium
链接：https://leetcode.com/problems/add-two-numbers/description/
描述：给两个非空链表，每个节点存一个0-9的整数，具体看例子吧
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return self.val


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        head = temp_node = ListNode(0)
        while l1 or l2 or carry:
            add = carry
            if l1:
                add += l1.val
                l1 = l1.next
            if l2:
                add += l2.val
                l2 = l2.next
            temp_node.next = ListNode(add % 10)
            temp_node = temp_node.next
            carry = add / 10
        return head.next

    def addTwoNumbers2(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = self.to_int(l1)
        num2 = self.to_int(l2)
        res = self.to_list(num1+num2)
        return res

    def to_int(self, l1):
        res = 0
        times = 1
        while l1:
            res += l1.val * times
            times *= 10
            l1 = l1.next
        return res

    def to_list(self, val):
        val = str(val)
        head = node = ListNode(int(val[-1:]))
        val = val[:-1]
        for x in val[::-1]:
            new_node = ListNode(int(x))
            node.next = new_node
            node = new_node
        return head

if __name__ == '__main__':
    node1 = ListNode(2)
    node2 = ListNode(4)
    node3 = ListNode(3)
    node4 = ListNode(5)
    node5 = ListNode(6)
    node6 = ListNode(4)

    node1.next = node2
    node2.next = node3

    node4.next = node5
    node5.next = node6

    print Solution().to_int(node1)
    print Solution().to_int(node4)

    res_node = Solution().addTwoNumbers(node1, node4)
    print res_node.val
    print res_node.next.val
    print res_node.next.next.val
    print Solution().to_int(res_node)