# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)
# print(7)
# print(8)
# print(9)
# print(10)

# while(9==9):
#     print("ok")

# i = 0

# while(i<5):
#     print(i)
#     i+=1 # i=i+1

n = 50

# while(n>0): #(50>0)-> returns TRUE
#     print(n)
#     n=n-1 #n-=1

"""
50
49
48
47
...
1
"""

k=25

# while(0<k): #0<25-> True 
#     print(k)
#     if(k==15):
#         continue
#     k=k-1 

"""
while(0<k): 
    k=k-1
    if k==15: 
        continue
    
    print(k)"""

k=0
while(k<20):
    k=k+1
    if k==15:
        continue
    # print(k)

if(9>8):
    pass

def funcName(params):
    pass
# while True:
#     pass

# FOR LOOP
shopping = ['Amazon', 'FlipKart', 'Walmart']
for company in shopping:
    print(company)

numbers = list(range(100, 501, 2))
print(numbers)
# print(numbers)
for num in numbers:
    # print(num)
    if num==300:
        break
else:
    print("completed")