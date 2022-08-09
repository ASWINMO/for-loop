vowels_and_constants=['a','e','i','o','u','r','t','A','H','K']
vowels=['a','e','i','o','u']
vowels_list=[]
constants_list=[]
for i in vowels_and_constants:
    i=i.lower()
    if i in vowels:
        vowels_list.append(i)
    else:
        constants_list.append(i)
print(vowels_list)
print(constants_list)