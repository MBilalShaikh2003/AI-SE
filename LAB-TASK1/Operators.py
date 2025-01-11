#1)
x=6
if(type(x) is int):
    print("true")
else:
    print("false")

#2)
y=7.2
if(type(y) is not int):
    print("true")    
else:
    print("false")

#3)
list1=[1,2,3,4,5]
list2=[6,7,8,9]
for item in list1:
    if item in list2:
        print("overlapping")
else:
    print("not overlapping")        



#4)Floor division and Exponent and Assign
# a//=3
# a**=5
# print("floor divide=",a)
# print("exponent=",a)


# Bitwise Operaotors:
# Define the values
a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101

# Bitwise AND
c = a & b  # 12 = 0000 1100
print("Line 1 - Value of c (a & b):", c)

# Bitwise OR
c = a | b  # 61 = 0011 1101
print("Line 2 - Value of c (a | b):", c)

# Bitwise XOR
c = a ^ b  # 49 = 0011 0001
print("Line 3 - Value of c (a ^ b):", c)

# Bitwise NOT
c = ~a  # -61 = 1100 0011 (in two's complement representation)
print("Line 4 - Value of c (~a):", c)

# Left shift
c = a << 2  # 240 = 1111 0000
print("Line 5 - Value of c (a << 2):", c)

# Right shift
c = a >> 2  # 15 = 0000 1111
print("Line 6 - Value of c (a >> 2):", c)
