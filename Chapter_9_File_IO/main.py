import cv2 #image processing
import numpy as np #image processing, operations on arrays
import custom

# f = open(r"D:\OceanProgrammer\tutorials\Python tutorial in one video\Chapter_9_File_IO\New folder\file.txt", 'r+')
# # data = f.read()
# # print(data)
# print(f.mode)
# print(f.name)
# print(f.closed)
# print(f.tell())
# f.seek(30)
# print(f.read(16))
# # name = input("Enter ur name: ")
# # for i in range(11):
# #     f.write(' good morning ')
# f.close()
# # print(f.closed)

# with open(r"D:\OceanProgrammer\tutorials\Python tutorial in one video\Chapter_9_File_IO\New folder\file.txt", 'r') as f:
#     print(f.read())

# print(custom.sum)
# print(custom.func(2))

## QUIZ
i = 0
print("WHILE LOOP:")
while(i<10):
    i=i+1
    print(f"8 * {i} = {8*i}")

print("FOR LOOP:")

for k in range(10):
    k=k+1
    print(f"8 * {k} = {8*k}")