string="Luminar is the BEst Institute"
lower_count=0
upper_count=0
space_count=0
for i in string:
    if i.isspace():
        space_count+=1
    elif i.islower():
        lower_count+=1
    else:
        upper_count+=1
print("lower_count",lower_count)
print("upper_count",upper_count)
print("space_count",space_count)