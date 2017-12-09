import unittest
from subprocess import Popen, PIPE, STDOUT
import string
import random
import os

def stringMaker(minSize=2, maxSize=10000, chars=string.ascii_uppercase + string.digits + " " + string.punctuation):
    randomSize = random.randint(minSize , maxSize)
    return ''.join(random.choice(chars) for _ in range(randomSize)) 

def TestBase():
    T = 10    
    ourIn = ''
    strings = []
    for i in range(T):
        strings.insert(i,stringMaker())
        ourIn += strings[i] + os.linesep
        
    stdIn = str(T) + os.linesep + ourIn
    p = Popen(['python', 'solution.py'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)   
    stdout = p.communicate(input=bytes(stdIn, encoding='utf-8'))[0]
    
    ourOut = ''
    for i in range(T):
        for j in range(0,len(strings[i]),2):
            ourOut += strings[i][j]
            
        ourOut += " "
        
        for j in range(1,len(strings[i]),2):
            ourOut += strings[i][j]
            
        ourOut += os.linesep
        
    expectedStdout = ourOut
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
