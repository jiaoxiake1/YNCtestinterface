#!/usr/bin/env python

import sys
sys.path.append('./mock_train')
import modular  #用装饰器时，不能from import 必须import
import unittest
from unittest import mock
# from .modular import Count # TestCount

# #  一 mock 一个函数
# class TestCount1(unittest.TestCase):
#
#     @mock.patch('modular.add_def')  #1 @mock.patch
#     def test_add(self,mock_add_def):  #2
#         mock_add_def.return_value = 3 #3
#         mock_add_def.side_effect = modular.add_def2
#         result = modular.add_def(1,2)
#
#         print(result)
#         self.assertEqual(result,6)


# 二 mock 对象中的一个方法

# class TestCount2(unittest.TestCase):
#
#     @mock.patch.object(modular.Count,'add')
#     def test_add(self,mock_add):
#         count = modular.Count()
#         mock_add.return_value = 3
#         mock_add.side_effect = count.add2
#         result = count.add(1,6)
#         print(result)
#         self.assertEqual(result,3)

#三 mock 多个函数注意顺序

# class TestCount3(unittest.TestCase):
#
#     @mock.patch.object(modular.Count,'add')
#     @mock.patch('modular.add_def')
#     def test_add(self,mock_add_def,mock_add): #参数的顺序和装饰器的顺序是相反的，与self是相同的
#         count =modular.Count()
#         mock_add_def.return_value = 12 #对应的result2
#         mock_add.return_value = 13
#         result1 =count.add(8,5)
#         result2 = modular.add_def(8,5)
#         self.assertEqual(result1,12)
#         self.assertEqual(result2,14)





# class TestCount(unittest.TestCase):
#
#     def test_add(self):
#         count = Count()
#
#         # count.add = mock.Mock(name='add') # name 为唯一标示
#         # count.add = mock.Mock(return_value=7,side_effect= count.add2)  # return_value 为唯一标示
#         # print(count.add)
#         result = count.add(8,5)
#         print(result)
#         self.assertEqual(result,13)

if __name__== '__main__':
    unittest.main()