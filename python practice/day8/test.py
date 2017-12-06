import os
import unittest
from subprocess import Popen, PIPE, STDOUT
import string
import random

def stringMaker(size = 5, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size)) 

def intMaker(min = 1 , max = 100000):
    return random.randint(min , max)
    
def phoneMaker():
    return str(random.randint(100,10000))

def TestBase():
    N = intMaker()
    ourIn = ''
    ourIn = str(N)+os.linesep
    validQuery = []
    phoneBook={}
    for i in range(N):
        name = stringMaker()
        number = phoneMaker()
        validQuery.insert(i,name)
        ourIn += name + " " + number + os.linesep
        phoneBook[name]=number
        
    query = []
    for i in range(len(validQuery)):
        query.append(validQuery[i])
        ourIn += validQuery[i] + os.linesep
        
    for i in range(100000-len(validQuery)):
        s = stringMaker()
        query.append(s)
        ourIn += s + os.linesep
        
    ourOut = ''
    for i in range(len(query)) :

        if query[i] in phoneBook :
            ourOut += query[i]+"="+phoneBook[query[i]]+os.linesep
        else:
            ourOut += "Not found"+os.linesep
            
    stdIn = ourIn
    p = Popen(['python', 'solution.py'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)   
    stdout = p.communicate(input=bytes(stdIn, encoding='utf-8'))[0]

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
