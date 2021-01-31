#! /usr/bin.python3
import unittest
import chrz
import random

class TestS(unittest.TestCase):

    def test_f0(self):
        self.assertTrue(True)

    def test_f1_1(self):
        w=chrz.f1(0)
        self.assertEqual(w,0)

    def test_f1_2(self):
        w=chrz.f1(1)
        self.assertEqual(w,1)

    def test_f1_3(self):
        w=chrz.f1(2)
        self.assertEqual(w,4)

    def test_f1_4(self):
        w=chrz.f1(2.1)
        self.assertEqual(w,5)

    def test_f1_5(self):
        w=chrz.f1(2.3)
        self.assertEqual(w,7)

    def test_f2_1(self):
        k=chrz.f2("ala")
        self.assertEqual(k,'a')

#    def test_f2_2(self):
#        k=chrz.f2([1,2,3])
#        self.assertEqual(k,1)

#    def test_f2_3(self):
#        k=chrz.f2([])
#        self.assertEqual(k,"BUUUM")
    def test_f3_1(self):
        k=chrz.f3(1)
        self.assertEqual(k, "jeden")
    def test_f3_2(self):
        k=chrz.f3(2)

        self.assertEqual(k,"dwa")
    def test_f3_3(self):
        k=chrz.f3(3)
        self.assertEqual(k,"trzy")
    def test_f3_4(self):
        k=chrz.f3(random.choice(range(4,1000)))
        self.assertEqual(k,"other")

    def test_f4_1(self):
        k=chrz.f4("ala")
        self.assertEqual(k,"ala ma kota")
    def test_f4_2(self):
        k=chrz.f4("kot")
        self.assertEqual(k,"kot ma ale")
    def test_f4_3(self):
        k=chrz.f4("kot", "psa")
        self.assertEqual(k,"kot ma kota i psa")
    def test_f4_4(self):
        k=chrz.f4("kot", "mysz")
        self.assertEqual(k,"kot ma kota i mysz")



if __name__ == '__main__':
        unittest.main()