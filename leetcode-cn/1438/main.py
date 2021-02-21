#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Authors: klin
Email: l33klin@foxmail.com
Date: 2021/2/21
"""


class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        max_len = 0
        left = right = 0
        cur_min = cur_max = nums[0]
        while right < len(nums):
            pass
        return max_len
        

if __name__ == '__main__':
    nums = [8,2,4,7]
    limit = 4
    print(Solution().longestSubarray(nums, limit))
