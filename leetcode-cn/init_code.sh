echo problems: $1
mkdir $1

echo link: $2
echo "#!/usr/bin/python
# -*- coding: utf-8 -*-
# refs: $2

import unittest


class TestSolution(unittest.TestCase):

    def test_(self):
        test_set = []
        for t in test_set:
            with self.subTest(i=t):
                pass


class Solution(object):

    pass


if __name__ == '__main__':
    unittest.main()
" > $1/main.py