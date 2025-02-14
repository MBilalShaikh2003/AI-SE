with open("cities.txt","w") as file:
    citys=int(input("Enter no cities: "))
    for i in range(citys):
        city=input("enter city name: ")
        pop=input("enter city population: ")
        mayor=input("enter city mayor: ")
        file.write(f"{city},{pop},{mayor} \n")
print("City data has been stored in 'cities.txt'.")



# Open the file in append mode
with open("student.txt", "a") as file:
    file.write("Now we are AI students\n")

print("Message appended successfully to 'student.txt'.")
