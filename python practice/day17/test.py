import unittest
from subprocess import Popen, PIPE, STDOUT
import string
import random

def string_generator(size=1, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size)) + " "+''.join(random.choice(chars) for _ in range(size))
		
def TestBase():
    stdIn = string_generator()
    p = Popen(['python', 'solution.py'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    stdout = p.communicate(input=bytes(stdIn, encoding='utf-8'))[0]
    expectedStdout = 1
    for i in range(0,int(stdIn[2])):
         expectedStdout = expectedStdout*int(stdIn[0])
    return (stdout.decode(), str(expectedStdout)+"\r\n")

	
class test(unittest.TestCase): 
    
    def testCase1(self):
        result = TestBase()
        self.assertEqual( result[0], result[1])
		
    def testCase2(self):
        result = TestBase()
        self.assertEqual( result[0], result[1])
		
    def testCase3(self):
        result = TestBase()
        self.assertEqual( result[0], result[1])
		
    def testCase4(self):
        result = TestBase()
        self.assertEqual( result[0], result[1])
		
    def testCase5(self):
        result = TestBase()
        self.assertEqual( result[0], result[1])
		
    def testCase6(self):
        result = TestBase()
        self.assertEqual( result[0], result[1])
		
    def testCase7(self):
        result = TestBase()
        self.assertEqual( result[0], result[1])
	
    def testCase8(self):
        result = TestBase()
        self.assertEqual( result[0], result[1])
		
    def testCase9(self):
        result = TestBase()
        self.assertEqual( result[0], result[1])
		
    def testCase10(self):
        result = TestBase()
        self.assertEqual( result[0], result[1])

if __name__ == '__main__':
    unittest.main()
