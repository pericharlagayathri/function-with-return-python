# Unit III - Experiment 30: Function with parameters and return value

def add_numbers(a, b):
    return a + b

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

result = add_numbers(first, second)

print("Sum =", result)
