#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Authors: klin
Email: l33klin@foxmail.com
Date: 2022/3/7
"""
import unittest
from typing import List
from ddt import data, ddt, unpack


class Solution:
    """My first try, Failed"""
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        rob_days = []
        if len(security) < time*2 + 1:
            return []
        pre_days_flag = after_days_flag = True
        now_day = time
        while now_day < len(security) - time:
            for i in range(now_day - time, now_day):
                if security[i+1] > security[i]:
                    pre_days_flag = False
                    now_day = i + time + 1
                    break
            if not pre_days_flag:
                pre_days_flag = True
                continue
            for i in range(now_day, now_day + time):
                if security[i+1] < security[i]:
                    after_days_flag = False
                    if i == now_day:
                        now_day += 1
                        # skip_pre_check = True
                    else:
                        now_day = i + time
                    break
            if after_days_flag:
                rob_days.append(now_day)
                now_day += 1
            pre_days_flag = after_days_flag = True

        return rob_days


class Solution1:
    """Solution from: https://leetcode-cn.com/problems/find-good-days-to-rob-the-bank/solution/gong-shui-san-xie-qian-zhui-he-yun-yong-gf604/"""
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        rob_days = []
        cp = [0]
        for i in range(1, len(security)):
            c = 0
            if security[i] > security[i - 1]:
                c = 1
            elif security[i] < security[i - 1]:
                c = -1
            else:
                c = 0
            cp.append(c)
        
        pre_l = [0]
        suf_l = [0]
        for i in cp[1:]:
            if i == 1:
                pre_l.append(pre_l[-1] + 1)
            else:
                pre_l.append(pre_l[-1])
            if i == -1:
                suf_l.append(suf_l[-1] + 1)
            else:
                suf_l.append(suf_l[-1])
        for i in range(time, len(security)-time):
            if pre_l[i] - pre_l[i - time] == 0 and suf_l[i + time] - suf_l[i] == 0:
                rob_days.append(i)
            
        return rob_days


@ddt
class TestSolution(unittest.TestCase):
    
    @data(([5, 3, 3, 3, 5, 6, 2], 2, [2, 3]),
          ([1, 1, 1, 1, 1], 0, [0, 1, 2, 3, 4]),
          ([1, 2, 3, 4, 5, 6], 2, []),
          ([1], 5, []),
          ([1, 1, 1, 1, 1], 0, [0, 1, 2, 3, 4]),
          ([4, 3, 2, 1], 1, []),
          # ([1, 2, 5, 4, 1, 0, 2, 4, 5, 3, 1, 2, 4, 3, 2, 4, 8], 2, [10, 14]),
          ([1, 2, 5, 4, 1, 0, 2, 4, 5, 3, 1, 2, 4, 3, 2, 4, 8], 2, [5, 10, 14]),
          ([1, 2, 5, 4, 2, 1, 2, 4, 3, 3, 1, 2, 4, 5, 2, 4, 8], 3, [10]),
          ([7]*100000, 25000, list(range(25000, 75000))))
    @unpack
    def test_case(self, security, _time, expect):
        got = Solution1().goodDaysToRobBank(security=security, time=_time)
        self.assertEqual(expect, got,
                         "\nexpect: {}\ngot: {}".format(expect, got))


unittest.main()
