# Generate a multiplication table using a loop
n = 1
num = int(input("Enter the table number: "))

while n < 11:
    print(f"{num} * {n} = {n * num}")
    n += 1
