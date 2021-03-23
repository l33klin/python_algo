#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    : main
@Purpose : 
@Author  : jian.li
@Contact : jian.li@shopee.com
@Time    : 2021/3/23 10:03 PM
@Refs    : https://leetcode-cn.com/problems/teemo-attacking/
"""
import unittest


class TestSolution(unittest.TestCase):

    def test_(self):
        test_set = [
            {
                "input": ([], 1),
                "output": 0
            },
            {
                "input": ([1], 1),
                "output": 1
            },
            {
                "input": ([1, 3], 2),
                "output": 4
            },
            {
                "input": ([1, 2], 2),
                "output": 3
            },
        ]
        for ts in test_set:
            with self.subTest(i=ts):
                self.assertEqual(Solution().findPoisonedDuration(*ts["input"]), ts["output"])


class Solution(object):

    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if len(timeSeries) == 0:
            return 0

        if len(timeSeries) == 1:
            return duration

        r = duration
        for i in range(len(timeSeries) - 1, 0, -1):
            r += min(timeSeries[i] - timeSeries[i-1], duration)
        return r


if __name__ == '__main__':
    unittest.main()


