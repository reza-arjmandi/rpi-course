import unittest
from subprocess import Popen, PIPE, STDOUT
import string
import random
from solution import Calculator

def string_generator(size=1, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size)) + " "+''.join(random.choice(chars) for _ in range(size))
		
def TestBase(n,p):
    calc = Calculator()
    pow = calc.power( n, p)
    return pow

	
class test(unittest.TestCase): 
    
    def testCase1(self):
        result = TestBase(2,4)
        self.assertEqual( 2**4, result)
		
    def testCase2(self):
        result = TestBase(3,1)
        self.assertEqual( 3**1, result)
		
    def testCase3(self):
        result = TestBase(9,9)
        self.assertEqual( 9**9, result)
		
    def testCase4(self):
        result = TestBase(7,2)
        self.assertEqual( 7**2, result)
		
    def testCase5(self):
        result = TestBase(4,11)
        self.assertEqual( 4**11, result)
		
    def testCase6(self):
        result = TestBase(3,6)
        self.assertEqual( 3**6, result)
		
    def testCase7(self):
        result = TestBase(7,8)
        self.assertEqual( 5764801, result)
	
    def testCase8(self):
        result = TestBase(1,10)
        self.assertEqual( 1, result)
		
    def testCase9(self):
        result = TestBase(5,10)
        self.assertEqual( 9765625, result)
		
    def testCase10(self):
        result = TestBase(2,4)
        self.assertEqual( 16, result)

if __name__ == '__main__':
    unittest.main()
