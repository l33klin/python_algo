#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/degree-of-an-array/
Authors: klin
Email: l33klin@foxmail.com
Date: 2021/2/20
"""


class Solution:
    
    def findShortestSubArray(self, nums: list[int]) -> int:
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = [1, i, i]
            else:
                d[nums[i]] = [d[nums[i]][0]+1, d[nums[i]][1], i]
        print(d)
        max_len = 0
        max_i = 0
        for k, v in d.items():
            if v[0] > max_len:
                max_len = v[0]
                max_i = k
            elif v[0] == max_len:
                max_i = k if (v[2] - v[1]) < (d[max_i][2] - d[max_i][1]) else max_i
        print(max_i)
        return d[max_i][2] - d[max_i][1] + 1
        

if __name__ == '__main__':
    nums = [1, 2, 2, 3, 1]
    print(Solution().findShortestSubArray(nums))
