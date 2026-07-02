try:
    num1,num2 = eval(input("Enter two numbers seperated by a comma: "))
    result = num1 / num2
    print("Result is",result)

except ZeroDivisionError:
    print("Divison by zero is error!")

except SyntaxError:
    print('comma is missing,enter numbers seperated by a comma')

except :
    print("wrong input")

else:
    print("no exception")

finally:
    print("This will execute no matter what.")