dict={1:"you",2:"me",3:"she"}
dict.update({4:"he"})
print(dict)
print("----------------")
dict["5"]="I"
print(dict)
dict.pop(1)
print(dict)
dict.popitem()
print(dict)
del dict[3]
print(dict)
dict.clear()
print(dict)