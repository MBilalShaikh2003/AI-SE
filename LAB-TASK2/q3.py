# (iii)The program must prompt the user for a username and password. The program should
# compare the password given by the user to a known password. If the password matches, the
# program should display “Welcome!” If it doesn’t match, the program should display “I don’t
# know you.
# Note: the password should not be case sensitive and it’s value is abc$123 or ABC$123

save="1234"
password=str(input("Enter Password: "))
if save==password:
    print("Welcome")
else:
    print("Incorrect Password")    

