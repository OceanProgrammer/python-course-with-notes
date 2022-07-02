# d1 = {"key": "value", "ch5": "dictionary and sets"}
# print(d1)
# print(d1["key"])
# # print(d1["Ch5"])
# # print(d1["ch6"])
# # print(d1[0])
# d1["Elon Musk"] = "Telsa"
# print(d1)
# print(d1["Elon Musk"])

# d2 = d1.copy()
# d2["Steve Jobs"] = "Apple"
# print(d1)
# print(d2)
dict = {"Toothbrush": "Colgate",
        "Spectales": "LensKart",
        "Shoes": "Nike",
        "PC": "HP",
        "Mobile Phone": {"Apple": "iPhone",
                         "Samsung": "Android",
                         "OnePlus": "OxygenOS"}}

print(dict)
print(dict["Mobile Phone"]["OnePlus"])
dict.update({"Car": "Rolls Royce"})
# print(dict.keys())
keys = list(dict.keys())
# print(keys[0])

values = list(dict.values())
# print(values[4])
newD = values[4]
newD_keys = list(newD.keys())
# print(newD_keys[0])
print(dict.items())
print(dict.get("Shoes3"))
# print(dict["asdfds"])
# dict.clear()
dict.pop("Mobile Phone")
dict.popitem()
print(dict)

mySet = {2,3,5,7,11,13,13,13,13,13,13,13, 17}
mySet2 = {11, 17, 7, 23, 29}
print(mySet)

emptySet = set()
print(type(emptySet))
print(len(mySet))
mySet.add(19)
mySet.remove(13)
print(mySet.union(mySet2))
print(mySet.intersection(mySet2))
print(mySet.isdisjoint(emptySet))
print(mySet.symmetric_difference(mySet2))
print(mySet.discard(3))
mySet.clear()
print(mySet)