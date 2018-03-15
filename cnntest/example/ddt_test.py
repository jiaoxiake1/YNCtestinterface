#!/usr/bin/env python
import unittest
# from practise.myTestPractice.api_login import *
import ddt


@ddt.ddt
class Praddt(unittest.TestCase):

    def setUp(self):
        print("my test start！")

    def tearDown(self):
        print("my test complete!")

    def add(self,a,b):
        return a+b

    @ddt.data([2, 1, 3,"success"],
              [1, 1, 1,"error"]
             )
    @ddt.unpack
    def test_ddt1(self, user, passwd, expect_value,zhuangtai):
        result = self.add(user, passwd)
        self.assertEqual(result, expect_value, msg=zhuangtai)

    # def test_ddt2(self, user, passwd, expect_value, zhuangtai):
    #     result = self.add(user, passwd)
    #     self.assertEqual(result, expect_value, msg=zhuangtai)