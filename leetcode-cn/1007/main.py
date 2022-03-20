#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
Authors: klin
Email: l33klin@foxmail.com
Date: 3/20/22
"""
import unittest
from typing import List
from ddt import ddt, data, unpack


class Solution:
    """Solution1"""
    
    def solution1(self, arg1: List[int], arg2: int) -> List[int]:
        pass


@ddt
class TestSolution(unittest.TestCase):
    
    @data(
        ([5, 3, 3, 3, 5, 6, 2], 2, [2, 3]),
        ([1, 1, 1, 1, 1], 0, [0, 1, 2, 3, 4]))
    @unpack
    def test_case(self, security, _time, expect):
        got = Solution().solution1(arg1=security, arg2=_time)
        self.assertEqual(expect, got,
                         "\nexpect: {}\ngot: {}".format(expect, got))


unittest.main()