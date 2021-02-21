#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/add-two-numbers/
Authors: klin
Email: l33klin@foxmail.com
Date: 2021/2/20
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __repr__(self):
        if not self.next:
            return "{}".format(self.val)
        return "{}->{}".format(self.val, self.next)


class Solution:
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = l1
        carry = 0
        while l1:
            tmp = carry + l1.val
            # tmp += l1.val if l1 else 0
            tmp += l2.val if l2 else 0
            l1.val = tmp % 10
            carry = int(tmp/10)

            if l1.next:
                l1 = l1.next
                if l2:
                    l2 = l2.next
                elif carry:
                    print(result)
                    continue
                else:
                    break
            elif l2:
                if not l2.next:
                    if carry:
                        l1.next = ListNode(val=1)
                        break
                l1.next = l2.next
                l2 = None
                l1 = l1.next
            else:
                if carry:
                    l1.next = ListNode(val=1)
                break
                
        return result


def convert_int_to_list(a: int) -> ListNode:
    head = ListNode(val=a % 10)
    tail = head
    while int(a/10) > 0:
        a = int(a/10)
        tail.next = ListNode(val=a % 10)
        tail = tail.next
    
    return head


if __name__ == '__main__':
    a = 5
    b = 5
    la = convert_int_to_list(a)
    lb = convert_int_to_list(b)
    lc = Solution().addTwoNumbers(la, lb)
    print((str(a+b))[::-1])
    print(lc)
