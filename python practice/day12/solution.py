class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber

	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)


class Student(Person):
        # firstName: A string denoting the Person's first name.
        # lastName: A string denoting the Person's last name.
        # idNumber: An integer denoting the Person's ID number.
        # scores: An array of integers denoting the Person's test scores.
	def __init__(self, firstName, lastName, idNumber, scores):
		super().__init__(firstName, lastName, idNumber)
		self.scores = scores
	
    # Calculate a Student object's average 
	def calculate(self):
		average = sum(self.scores) / len(self.scores)
		# Return the character denoting the grade.
		if average < 40:
			return "T"
		elif (40 <= average) and (average < 55):
			return "D"
		elif (55 <= average) and (average < 70):
			return "P"
		elif (70 <= average) and (average < 80):
			return "A"
		elif (80 <= average) and (average < 90):
			return "E"
		elif (90 <= average) and (average <= 100):
			return "O"
		else:
			return " "

# Printout the personal datas
line = input().split()
firstName = line[0]
lastName = line[1]
idNumber = line[2]
numScores = int(input()) 
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNumber, scores)
s.printPerson()
print("Grade:", s.calculate())
