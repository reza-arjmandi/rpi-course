import unittest
from subprocess import Popen, PIPE, STDOUT
import random
import os

def int_generator(min=0, max=1000):
    return random.randint(min, max)


def TestBase():      
    N = int_generator()
    ourIn = ''
    ourOut = ''
    numberInput = []
    
    for i in range(N):
        numberInput.insert(i,int_generator())    
        ourIn += str(numberInput[i]) + " "

    for i in range(N):
        ourOut += str(numberInput[N-i-1]) + " "
                
        
    stdIn = str(N) + os.linesep + ourIn + os.linesep
    p = Popen(['python', 'solution.py'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    stdout = p.communicate(input=bytes(stdIn, encoding='utf-8'))[0]

    expectedStdout = ourOut
    return (stdout.decode(), expectedStdout)


class test(unittest.TestCase):
    def testCase1(self):
        result = TestBase()
        self.assertEqual(result[0], result[1])

    def testCase2(self):
        result = TestBase()
        self.assertEqual(result[0], result[1])

    def testCase3(self):
        result = TestBase()
        self.assertEqual(result[0], result[1])

    def testCase4(self):
        result = TestBase()
        self.assertEqual(result[0], result[1])

    def testCase5(self):
        result = TestBase()
        self.assertEqual(result[0], result[1])

    def testCase6(self):
        result = TestBase()
        self.assertEqual(result[0], result[1])

    def testCase7(self):
        result = TestBase()
        self.assertEqual(result[0], result[1])

    def testCase8(self):
        result = TestBase()
        self.assertEqual(result[0], result[1])

    def testCase9(self):
        result = TestBase()
        self.assertEqual(result[0], result[1])

    def testCase10(self):
        result = TestBase()
        self.assertEqual(result[0], result[1])


if __name__ == '__main__':
    unittest.main()
