from __future__ import print_function
import unittest

def ExponentCalc(x,y):
	return x ** y

class ExponentCalcTest(unittest.TestCase):
	def testSuccess(self):
		result = ExponentCalc(5,4)
		self.assertEqual(result, 624)

	def testFailure(self):
		result = ExponentCalc(3,8)
		self.assertNotEqual(result, 6560)

unittest.main()