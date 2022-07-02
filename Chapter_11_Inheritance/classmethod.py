class Person:
    age = 32

    @classmethod
    def newAge(cls, new, other):
        cls.age = new
        cls.other = other

h = Person()
print(h.age)
h.newAge(55, 62)
print(h.age)
print(h.other)