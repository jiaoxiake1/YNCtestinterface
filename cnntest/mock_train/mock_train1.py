#!/usr/bin/env python

import sys
sys.path.append('./mock_train')
import modular  #用装饰器时，不能from import 必须import
import unittest
from unittest import mock
from .modular import Count # TestCount







class TestCount(unittest.TestCase):

    def test_add(self):
        count = Count()

        # count.add = mock.Mock(name='add') # name 为唯一标示
        count.add = mock.Mock(return_value=7,side_effect= count.add2)  # return_value 为唯一标示
        # print(count.add)
        result=count.add(8,5)
        # print(result)
        count.add.assert_called_with(8,5)
        print(count.add.called)
        self.assertEqual(result,13)


if __name__== '__main__':
    unittest.main()