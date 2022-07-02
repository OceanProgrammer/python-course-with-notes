class School:
    students = 2000
    new = 200

    @property # getter decorator
    def newSession(self):
        return self.students + self.new

    # def newStudents(self, newSession):
    #     new = newSession - self.students
    #     print(new)
    @newSession.setter
    def newSession(self, newSession):
        self.new = newSession - self.students
        print(self.new)

h = School()
# print(h.newSession)
# h.newStudents(3000)
print(h.new)
# h.newSession()
