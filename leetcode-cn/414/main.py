#!/usr/bin/python
# -*- coding: utf-8 -*-
# refs: https://leetcode-cn.com/problems/third-maximum-number/

import unittest


class TestSolution(unittest.TestCase):

    def test_(self):
        test_set = [
            {
                "i": [2, 3, 1],
                "o": 1
            },
            {
                "i": [1, 2],
                "o": 2
            },
            {
                "i": [1, 2, 2, 3],
                "o": 1
            },
            {
                "i": [2, 2, 3],
                "o": 3
            },
            {
                "i": [1, 1, 2],
                "o": 2
            },
            {
                "i": [14],
                "o": 14
            }
        ]
        for t in test_set:
            with self.subTest(i=t):
                self.assertEqual(Solution().thirdMax(t["i"]), t["o"])


class Solution(object):

    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        biggest_3 = []
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(*nums)
        # elif len(nums) == 3:
        #     return min(*nums)

        for i in nums:
            if i in biggest_3:
                continue
            if len(biggest_3) < 3:
                biggest_3.append(i)
                biggest_3 = sorted(biggest_3, reverse=True)
                continue
            biggest_3.append(i)
            biggest_3 = sorted(biggest_3, reverse=True)[:3]

        if len(biggest_3) < 3:
            return biggest_3[0]
        return biggest_3[-1]



if __name__ == '__main__':
    unittest.main()
