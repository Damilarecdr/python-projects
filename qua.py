import math

# Input coefficients
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculate the discriminant (the value inside the square root)
discriminant = b**2 - 4*a*c
r = math.sqrt(discriminant)

# Check if the discriminant is positive, zero, or negative
if discriminant > 0:
    # Two real and distinct solutions1
    
    root1 = (-b + r) / (2*a)
    root2 = (-b - r) / (2*a)
    print("Two real and distinct solutions:")
    print(f"Root 1: {root1}")
    print(f"Root 2: {root2}")
elif discriminant == 0:
    # One real solution (repeated root)
    root = -b / (2*a)
    print("One real solution (repeated root):")
    print(f"Root: {root}")
else:
    # Complex solutions
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
    print("Complex solutions:")
    print(f"Root 1: {real_part} + {imaginary_part}i")
    print(f"Root 2: {real_part} - {imaginary_part}i")
