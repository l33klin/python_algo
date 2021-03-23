#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    : main
@Purpose : 
@Author  : jian.li
@Contact : jian.li@shopee.com
@Time    : 2021/3/23 9:59 PM
@Refs    : https://leetcode-cn.com/problems/max-consecutive-ones/submissions/
"""


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = 0
        tmp = 0
        for i in nums:
            if i == 1:
                tmp += 1
            else:
                r = max(r, tmp)
                tmp = 0
        r = max(r, tmp)
        return r


if __name__ == '__main__':
    print(Solution().findMaxConsecutiveOnes([1]))
