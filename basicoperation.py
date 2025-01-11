# Question1:Write a Python program to swap 4 variables values (input four values.
# Sample input:
# Before swapping
# a=2,b=56,c=78,d=9
# After Swapping
# a=,9,b=78,c=56,d=2

# Input four values
a = int(input("Enter the value for a: "))
b = int(input("Enter the value for b: "))
c = int(input("Enter the value for c: "))
d = int(input("Enter the value for d: "))

# Display values before swapping
print("\nBefore swapping")
print(f"a={a}, b={b}, c={c}, d={d}")

# Perform the swapping
a, b, c, d = d, c, b, a

# Display values after swapping
print("\nAfter swapping")
print(f"a={a}, b={b}, c={c}, d={d}")


# Question2: Write a Python program to convert temperatures to and from celsius,
# Fahrenheit.
# Formula : c/5 = f-32/9
# Expected Output :
# Enter temp in Celsius: 60°C
# Temperature in Fahrenheit is :140

# Input temperature in Celsius
cel = int(input("Enter temperature in Celsius: "))

# Display temperature in Celsius
print(f"Temperature in Celsius: {cel}°C")

# Convert Celsius to Fahrenheit
fer = (9 / 5) * cel + 32

# Display temperature in Fahrenheit
print(f"Temperature in Fahrenheit: {fer}°F")
