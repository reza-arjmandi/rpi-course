import unittest
from subprocess import Popen, PIPE, STDOUT
import string
import random
import os

def int_generator(min=0, max=100000):
    return random.randint(min, max)
		
def TestBase():
    stdIn = int_generator()
    result = ""
    if(stdIn % 2 != 0):
        result = "Weird"
	
    if(stdIn % 2 == 0 and (stdIn>=2 and stdIn<=5)):
        result = "Not Weird"
	
    if(stdIn % 2 == 0 and (stdIn>=6 and stdIn<=20)):
        result = "Weird"

    if(stdIn % 2 == 0 and stdIn>20):
        result = "Not Weird"
    
    p = Popen(['python', 'solution.py'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)   
    stdout = p.communicate(input=bytes(str(stdIn), encoding='utf-8'))[0]
    expectedStdout = result + os.linesep
    return (stdout.decode(), expectedStdout)
	
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
