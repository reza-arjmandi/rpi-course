import unittest
from subprocess import Popen, PIPE, STDOUT
import string
import random

def string_generator(size=6, chars=string.ascii_uppercase + string.digits + " " + string.punctuation):
    return ''.join(random.choice(chars) for _ in range(size))

def int_generator(min=0, max=100000):
    return random.randint(min, max)

def real_generator(min=0.0, max=100000.0):
    return random.uniform(min, max)

def TestBase():
    randInt = int_generator()
    randReal = real_generator()
    randStr = string_generator()
    i = 4
    d = 4.0
    s = 'HackerRank '

    stdIn = str(randInt) + "\r\n" + str(randReal) + "\r\n" + str(randStr) + "\r\n"
    p = Popen(['python', 'solution.py'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)   
    stdout = p.communicate(input=bytes(stdIn, encoding='utf-8'))[0]
    expectedStdout = str(randInt + i) + "\r\n" + str(randReal + d).format("{:0.1}") + "\r\n" + s + randStr + "\r\n"
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
