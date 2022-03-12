#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Authors: klin
Email: l33klin@foxmail.com
Date: 3/12/22
"""
import unittest
from ddt import ddt, data, unpack
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
        
    def __repr__(self):
        if self.children:
            return "({})->>{}".format(self.val, self.children)
        else:
            return "({})".format(self.val)
    

def list_to_node2(node_list: list) -> Node:
    root = Node(val=node_list[0], children=[])
    up_lv_ref = [root]
    cur_lv_ref = []
    up_lv_num = 1
    for i in range(2, len(node_list)):
        if node_list[i] is None:
            up_lv_num -= 1
            if up_lv_num == 0:
                up_lv_ref = cur_lv_ref
                up_lv_num = len(cur_lv_ref)
                cur_lv_ref = []
                continue
        else:
            new_node = Node(val=node_list[i], children=[])
            up_lv_ref[len(up_lv_ref) - up_lv_num].children.append(new_node)
            cur_lv_ref.append(new_node)
    return root
            

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        if not root.children:
            return [root.val]
        else:
            result = []
            for child in root.children:
                result += self.postorder(child)
            return result + [root.val]


@ddt
class TestSolution(unittest.TestCase):
    
    @data(
        ([1, None, 3, 2, 4, None, 5, 6], [5, 6, 3, 2, 4, 1]),
        ([1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10, None, None, 11, None, 12, None, 13, None, None, 14], [2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9, 10, 5, 1])
    )
    @unpack
    def test_solution(self, node_list, expect):
        node = list_to_node2(node_list)
        got = Solution().postorder(node)
        self.assertEqual(expect, got, "expect: {}\ngot: {}".format(expect, got))


unittest.main()
