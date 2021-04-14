class Student:
    grade = 0
    passing_grade = 75
    award_credit = False
    
    def __init__(self, first, last):
        self.first = first #These are instance variables
        self.last = last
        self.email = first + last + '@mail.weber.edu'
    
    #Behavior
    def printStudentInfo(self):
        print('\nFull Name:', self.first, self.last, '\nEmail:', self.email, '\nGrade:', self.grade, '\nAward Credit:', self.award_credit, '\n')

    def passingClass(self):
        if self.grade < self.passing_grade:
            self.award_credit = False
        else:
            self.award_credit = True
    
    def setGrade(self, grade):
        self.grade = grade
        self.passingClass()
        
    def extraCredit(self, points):
        self.grade = self.grade + points
        self.passingClass()

    @classmethod
    def setPassingGrade(cls, grade):
        cls.passing_grade = grade




