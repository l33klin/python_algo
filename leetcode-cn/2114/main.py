#!/usr/bin/python
# -*- coding: utf-8 -*-
# refs: https://leetcode-cn.com/problems/maximum-number-of-words-found-in-sentences/

import unittest
from typing import List


class TestSolution(unittest.TestCase):

    def test_(self):
        pass


class Solution(object):
    
    def mostWordsFound(self, sentences: List[str]) -> int:
        result = 0
        for sentence in sentences:
            if len(sentence) == 0:
                continue
            w_count = 1
            for c in sentence:
                if c == " ":
                    w_count += 1
            result = max(result, w_count)

        return result


if __name__ == '__main__':
    unittest.main()

