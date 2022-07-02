from datetime import datetime
import new
# n = int('9') # n is object of class int
# s = list["something"] # s is object of class list

class Watch: # attributes, functions
    # waterproof = True
    # company = "Titan"

    # @staticmethod
    def getTime(self):
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        print(f"Current time is {time}")
        
    # def getInfo(self):
    #     return f"Company of your watch is {self.company}. It costs Rs. {self.price}.\n Your watch is of {self.type} type.\n THANK U SIR!"

    def __init__(self, company, price): # self-object; company-
        self.brand = company
        self.cost = price
        print(f"Company is {self.brand}\nPrice is {self.cost}.\n")

myWatch = Watch("sonata", 1000)
# myWatch.company = "Sonata" # 'company' attribute changed here
# print(type(myWatch))
# print(Watch.waterproof)
# print(f"Company of watch is {Watch.company}")
# print(f"Company of my watch is {myWatch.company}")
# myWatch.price = 1000
# print(myWatch.price)
# print(Watch.price)

# Watch.type = "dial"
# print(myWatch.type)

# myWatch.type = "Analog"
# print(myWatch.type)

# print("\n")
# newWatch = Watch()
# newWatch.company = "Rolex"

myWatch.getTime()
# print(myWatch.getInfo())
"""
self.company -> myWatch.company
self.price -> myWatch.price
self.type -> myWatch.type
"""
print(myWatch.__dict__)
print(new.__name__)

k = 56 #global variable

def funcName():
    # k = 34
    i = 98 #local variable
    i+=3
    global k
    k=k+1
    print("new-", k)
print(k)
funcName()

print(Watch.getTime(myWatch))