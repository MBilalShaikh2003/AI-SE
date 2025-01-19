# Exercise 1:
# (I)Cabinets and Boxes are objects that are mostly in cubic shape. Make a program that takes
# inputs like height, width and depth from user and then calculate volume of the cube:
# volume = height ∗ width ∗ depth


height=int(input("enter height: "))
width=int(input("enter width: "))
depth=int(input("enter depth: "))
volume=height*width*depth
print("The volume is : ",volume ,"cm3")
if 1<=volume<=10:
    print("Extra Small") 
elif 11<=volume<=20:
    print("Small")
elif 21<=volume<=30:
    print("Medium")
elif 31<=volume<=40:
    print("Large")
elif 41<=volume<=50:
    print("Extra Large")
else:
    print("Extra Extra Large")