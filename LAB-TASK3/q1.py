number=[1,2,3]
print("square:")
x=lambda n:n**2
for n in number:
    print(x(n))
print("cube:")
y=lambda y:y**3
for i in number:
    print(y(i))