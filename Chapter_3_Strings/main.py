# s = "this is a string"
# print(type(s))
# print(type(1))

str_with_single_qu = 'str"ing'
print(str_with_single_qu)

str_with_double_qu = "str'ing"
print(str_with_double_qu)

str_with_three_single_qu = '''This 
i"""
s a string'''
print(str_with_three_single_qu)

str_with_three_double_qu = """This is""
double quoted var"""
print(str_with_three_double_qu)

print("\n")

print("text "*5)
# print("text "*"5")

# var1 = "Programming"
# print(len(var1))
# print(var1[4])
# print(var1[-4])
# # print("video"[5])
# print(var1[1:77]) # Get till: [0:(num-1)]
# var2 = "Twitter" #Titr
# print(var2[0:len(var2):2]) #2-1->1
word = "alUmi niUM13"
print(word[0:])
print(word[:5])
print(word[::-1])

## STRING FUNCTIONS
word = "alUmi niUM13"

# print(len(word))
# print(word.isalnum())
# print(word.endswith("ium13"))
# print(word.count('i'))
# print(word.capitalize())
# print(word.find("niUM13"))
# print(word.lower())
# print(word.upper())
word2 = word.replace("niUM13", "ok")
print(word2)
