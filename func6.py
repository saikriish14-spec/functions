import math 
def area (a):
    area = math.pi * a ** 2 
    print(f"{area}")
    
area(10)


# area of the rectangle

def area_rectangle(length,width):
    f1 = length * width 
    print(f"the area of the rectangle is {f1}")

area_rectangle(100,32)



# cube number 

def cube (a):
    cube = a ** 3 
    print(f"the cubed of this number is {cube}")

cube(3)


#perimeter of rectangle

def rectangle_perimeter (a,b):
    result = (a+b)*2
    print(f"the perimeter is {result}")

rectangle_perimeter(2,5)



# area of triangle

def triangle_area(base, height):
    result = (base * height) / 2
    print(f"The area of the triangle is {result}")

triangle_area(12, 2)


# multiply 2 numbers 

def multiplication (num1,num2):
    result = num1 * num2
    print(f"the multiplication of 2 numbers is {result}")

multiplication(2,4)

# add 2 numbers

def addition(num1,num2):
    result = num1 + num2 
    print(f"the sum of num1 and num2 is {result}")

addition(100,200)



# subtract two numbers
def subtraction(num1,num2):
    result = num2 - num1
    print(f"the value of num2 - num1 = {result }")


# division of 2 numbers 

def division(num1,num2):
    result = num2/num1
    print(f"the divison of both of these are {result}")

division(50,100)


# average

def average(num1,num2,num3):
    result = (num1+num2+num3)/3
    print(f"the average of num1 num2 and num3 is {result}")

average(100,200,300)


def multiplication(a, b):
    result = a * b
    return result

answer = multiplication(2, 4)

print(answer)             


    