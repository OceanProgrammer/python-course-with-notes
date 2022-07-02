class A:
    job = "Business"
class B(A):
    city = "San Francisco"
class C(B):
    dob = "24 February 1955"

a = A()
b = B()
c = C()
A.name = "Steve Jobs"
print(a.name)
print(b.name)
print(c.name)