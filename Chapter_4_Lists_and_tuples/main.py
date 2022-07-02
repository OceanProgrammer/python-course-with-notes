companies = ["Tesla", "Google", "Microsoft", "Titan", "Apple", 9, 7]
companies[0] = "Tata"
empty_list = []
# print(companies)
# print(companies[::-1])

# new_l = companies[0:6]
# print(new_l)
"""
COMPANY-INDEX
Tesla-0
Google-1
Microsoft-2
Titan-3
Apple-4
9-5
7-6
"""
# # print(companies)
# print(type(companies))
# print(len(companies))
# print(companies[5])

# # cons_list = list("boAt")
# # print(cons_list)
# # print(cons_list[3])

# l = [43, 34,21,92, 11, 39]
# # l.sort(reverse=True)
# # l.reverse()
# # print(len(l))
# # print(l)
# print(max(l))
# print(min(l))
# l.append(100)
# print(len(l))
# l.insert(4, 55)
# print(l, "-", len(l))
# l.remove(100)
# print(l, "-", len(l))
# l.pop()
# l.clear()
# print(l)

tu = 2,4,6,2,2,2,2,2
print(tu)
print(tu.count(2))
print(tu.index(2))
# tu[0] = 9
print(type(tu))
emp_tp = ()
print(emp_tp)
print(type(emp_tp))
myTp = (1,)
print(type(myTp))
print(myTp)
cons_tp = tuple("Lenovo")
print(cons_tp[0])

# QUESTION
age1 = int(input("Enter your age: "))
age2 = int(input("Enter your age: "))
age3 = int(input("Enter your age: "))
age4 = int(input("Enter your age: "))
age5 = int(input("Enter your age: "))

ages_list = [age1,age2,age3,age4,age5]
print(ages_list)
print("Maximum age is: ",max(ages_list))
print("Minimum age is: ",min(ages_list))