import unittest
from subprocess import Popen, PIPE, STDOUT
import string
import random
import os

def string_generator(size=6, chars=string.ascii_uppercase + string.digits + " " + string.punctuation):
    return ''.join(random.choice(chars) for _ in range(size))
		
def TestBase():
    stdIn = "4" + os.linesep  + "-1" + os.linesep + "10" + os.linesep + "16" + os.linesep + "18" + os.linesep
    p = Popen(['python', 'solution.py'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)   
    stdout = p.communicate(input=bytes(stdIn, encoding='utf-8'))[0]
    expectedStdout = "Age is not valid, setting age to 0." + os.linesep
    expectedStdout += "You are young." + os.linesep + "You are young." + os.linesep + os.linesep
    expectedStdout += "You are young." + os.linesep + "You are a teenager." + os.linesep + os.linesep
    expectedStdout += "You are a teenager." + os.linesep + "You are old." + os.linesep + os.linesep
    expectedStdout += "You are old." + os.linesep + "You are old." + os.linesep + os.linesep
    return (stdout.decode(), expectedStdout)
	
class test(unittest.TestCase): 
    
    def testCase1(self):
        result = TestBase()
        self.assertEqual(result[0], result[1])

if __name__ == '__main__':
    unittest.main()
