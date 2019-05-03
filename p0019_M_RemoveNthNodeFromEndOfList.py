# -*- coding: utf-8 -*-
# @Time    : 2019/5/3 10:56
# @Author  : Yulong Liu
# @File    : p0019_M_RemoveNthNodeFromEndOfList.py


"""
题号：19
难度：medium
链接：https://leetcode.com/problems/remove-nth-node-from-end-of-list/
描述：删除给定链表的倒数第 n 个节点
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return self.__str__()

    def __bool__(self):
        return bool(self.val)


def traversing(head: ListNode) -> None:
    """遍历这个链表"""
    if not head:
        print('traversing', [])
        return None
    current = head
    path = [current.val]
    while current.next:
        current = current.next
        path.append(current.val)
    print('traversing', path)
    return None


def build(n: int) -> ListNode:
    """按顺序生成一个链表"""
    if n < 1:
        return ListNode(0)
    head = ListNode(1)
    current = head
    for i in range(2, n + 1):
        current.next = ListNode(i)
        current = current.next
    return head


class Solution:
    def removeNthFromEnd1(self, head: ListNode, n: int) -> (ListNode, None):
        """注意：返回值可能是 ListNode 或 None
        边界值校验很重要，其他的，因为数据结构比较简单，时间上也就是一次遍历
        剩下的就是看空间上怎么优化了
        """
        if not head.next:
            return None

        current = head
        cache = [head]
        max_len = n + 1
        length = 1
        while current.next:
            current = current.next
            length += 1
            if len(cache) < max_len:
                cache.append(current)
            else:
                cache.pop(0)
                cache.append(current)

        if n == 1:  # 删最后一个
            cache[-2].next = None
        elif n == length:  # 删第一个
            return cache[1]
        else:  # 其他情况
            cache[0].next = cache[2]
        return head

    def removeNthFromEnd(self, head: ListNode, n: int) -> (ListNode, None):
        """看了 discuss，可以这样
        fast 和 slow 的差值为 n
        fast 遍历到最后时，slow所在的点就是要被删掉的
        """
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:  # 删第一个
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head


if __name__ == '__main__':
    node = build(2)
    traversing(node)
    x = Solution().removeNthFromEnd(node, 2)
    traversing(x)
