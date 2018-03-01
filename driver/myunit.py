#!/usr/bin/env python

import unittest

class MyTest(unittest.TestCase):

    base_url = "http://139.196.43.67:8080/"


    # def setUp(self,url):
    #     self.base_url = "http://139.196.43.67:8080/"
    #     return self.base_url

    def tearDown(self):
        print(self.result)
