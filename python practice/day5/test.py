import unittest
from subprocess import Popen, PIPE, STDOUT
import random
import os

def int_generator(min=0, max=100):
    return random.randint(min, max)

def TestBase():
    number = int_generator()
    answer=[]
    answer.append(number*1)
    answer.append(number*2)
    answer.append(number*3)
    answer.append(number*4)
    answer.append(number*5)
    answer.append(number*6)
    answer.append(number*7)
    answer.append(number*8)
    answer.append(number*9)
    answer.append(number*10)
    stdIn = str(number) + os.linesep
    p = Popen(['python', 'solution.py'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    stdout = p.communicate(input=bytes(stdIn, encoding='utf-8'))[0]

    result1  = "{} x 1 = {}".format(number, answer[0]) + os.linesep
    result2  = "{} x 2 = {}".format(number, answer[1]) + os.linesep
    result3  = "{} x 3 = {}".format(number, answer[2]) + os.linesep
    result4  = "{} x 4 = {}".format(number, answer[3]) + os.linesep
    result5  = "{} x 5 = {}".format(number, answer[4]) + os.linesep
    result6  = "{} x 6 = {}".format(number, answer[5]) + os.linesep
    result7  = "{} x 7 = {}".format(number, answer[6]) + os.linesep
    result8  = "{} x 8 = {}".format(number, answer[7]) + os.linesep
    result9  = "{} x 9 = {}".format(number, answer[8]) + os.linesep
    result10 = "{} x 10 = {}".format(number, answer[9])+ os.linesep
    
    expectedStdout = result1+result2+result3+result4+result5+result6+result7+result8+result9+result10 
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
