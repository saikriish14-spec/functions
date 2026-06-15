import math 

def volume_cone(radius,height):
    f1 = (1/3) *math.pi *radius **2 * height
    print(f"the volume of the cone is {f1}")


while True:
    f1 = int(input("Enter the radius:"))
    f2 = int(input("Enter the height "))
    volume_cone(f1,f2)



 





