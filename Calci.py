  
while True:
    print("Choose your arithmetic function:")
    print("1. sum")
    print("2. subtratct")
    print("3. multiply")
    print("4. divide")

    ch = int(input("Enter your choice: "))

    num1 = float(input("Enter a number num1:"))
    num2 = float(input("Enter a numbr num2:"))


    if ch == 1:
        sum = num1 + num2
        print(sum)

    elif ch == 2:
        subtract = num1 - num2
        print(subtract)
    elif ch ==3:
        multiply = num1 * num2
        print(multiply)
    else:
        if num2 > 0:
            divide = num1 / num2
            print(divide)
        else:
             print("Math Error")
        
        





    

    
