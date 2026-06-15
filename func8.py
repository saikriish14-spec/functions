def waiter_tip (num1,num2):
    result = num1 + 0.01 * num1 * num2 
    print(f"The tip that the waiter recieves is {result}")




while True:
    result = float(input("Enter the value of the bill"))
    tip = float(input("Enter the value of the tip"))
    waiter_tip(result,tip)
    next = input("Do you continue or leave?")
    if next == "y":
        print("Hi, you have chosen to continue.")
    else:
        break

    

