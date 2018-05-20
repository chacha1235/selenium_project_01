# coding=utf-8
import unittest
class TestAddCase(unittest.TestCase):
    u'''加法算术'''
    def add(self,a,b):
        return a+b
    def test_01(self):
        u'''1+1==2'''
        c=self.add(2,4)
        self.assertEqual(c,6)
if __name__=="__main":
    unittest.main()
