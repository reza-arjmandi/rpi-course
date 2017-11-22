import unittest
from subprocess import Popen, PIPE, STDOUT
import string
import random

def string_generator(size=6, chars=string.ascii_uppercase + string.digits + " " + string.punctuation):
    return ''.join(random.choice(chars) for _ in range(size))
		
def TestBase():
    stdIn = "4\r\n-1\r\n10\r\n16\r\n18\r\n"
    p = Popen(['python', 'solution.py'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)   
    stdout = p.communicate(input=bytes(stdIn, encoding='utf-8'))[0]
    expectedStdout = "Age is not valid, setting age to 0.\r\n"
    expectedStdout += "You are young.\r\nYou are young.\r\n\r\n"
    expectedStdout += "You are young.\r\nYou are a teenager.\r\n\r\n"
    expectedStdout += "You are a teenager.\r\nYou are old.\r\n\r\n"
    expectedStdout += "You are old.\r\nYou are old.\r\n\r\n"
    return (stdout.decode(), expectedStdout)
	
class test(unittest.TestCase): 
    
    def testCase1(self):
        result = TestBase()
        self.assertEqual(result[0], result[1])

if __name__ == '__main__':
    unittest.main()
