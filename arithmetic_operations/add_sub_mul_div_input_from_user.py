#add sub div mul input from user
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

if b != 0:
    print("Division:", a / b)
else:
    print("Division not possible (cannot divide by zero)")
    #Output
    """Enter first number: 22
Enter second number: 23
Addition: 45.0
Subtraction: -1.0
Multiplication: 506.0
Division: 0.9565217391304348"""
