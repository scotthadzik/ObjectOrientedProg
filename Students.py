class Student:
    def __init__(self, first, last, status):
        self.first = first #These are instance variables
        self.last = last
        self.status = status
        self.email = first + last + '@mail.weber.edu'
    
    #Behavior
    def printStudentInfo(self):
        print('Full Name:', self.first, self.last, '\nEmail:', self.email, '\nStatus:', self.status)

W01234 = Student('Scott', 'Hadzik','Pass') #instance of the Student Class
W01235 = Student('Waldo', 'Wildcat', 'Pass')

W01234.printStudentInfo()
W01235.printStudentInfo()

