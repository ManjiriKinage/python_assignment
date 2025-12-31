import math 

def add(a, b):
    return a + b

def subtract(a, b):   # fixed spelling
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


ans = 0   # initialize ans

while True:
    print("\n--- Calculator ---")
    print("1.Add  2.Sub  3.Mul  4.Div")
    print("5.Sin  6.Cos  7.Sqrt")
    print("0.Exit")
    
    ch = input("Enter choice: ")
    
    if ch == '0':
        print("Calculator closed")
        break

    if ch in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if ch == '1':
            ans = add(num1, num2)
        elif ch == '2':
            ans = subtract(num1, num2)
        elif ch == '3':
            ans = multiply(num1, num2)
        elif ch == '4':
            ans = divide(num1, num2)

        print("Result =", ans)

    elif ch in ['5', '6', '7']:
        num1 = float(input("Enter number: "))
        ans = num1

        if ch == '5':
            ans = math.sin(math.radians(ans))
        elif ch == '6':
            ans = math.cos(math.radians(ans))
        elif ch == '7':
            ans = math.sqrt(ans)

        print("Result =", ans)

    else:
        print("Invalid choice")
