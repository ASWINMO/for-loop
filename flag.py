num1=int(input("aswin enter a number1:"))
print(num1)

num2=int(input("aswin enter the another number2:"))
print(num2)
replace1=""
print("these are the operator you can use:")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
print("5.modulus")
result=0
operator=input("please choose an option from these (1,2,3,4,5):")
if operator=="1":
    result=num1+num2
    print("The result of addition of",num1,"and",num2,"is",result)
if operator=="2":
    if num1<num2:
        print("cannot calculate")
    else:
        result=num1-num2
        print("The result of subtraction of ",num1,"and",num2,"is",result)
if operator=="3":
    if num2==0 or num1==0:
        print("cannot multiply by zero")
    else:
        result=num1*num2
        print("The result of multiplication of",num1,"and",num2,"is",result)
if operator=="4":
    if num2==0:
        print("cannot divide by zero")
    else:
        result=num1//num2
        print("The result of division of",num1,"and",num2,"is",result)
if operator=="5":
    if num2==0:
        print("cannot modulus by zero ")
    else:
         result=num1%num2
    print("The result of modulus of",num1,"and",num2,"is",result)