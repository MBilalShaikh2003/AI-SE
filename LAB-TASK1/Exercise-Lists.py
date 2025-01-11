#Exploring list operations

lst=['a','b','c']
lst.reverse()
print(f"Reversed List:{lst}")

lst.append('d')
print(f"Appended List:{lst}")

count_a=lst.count('a')
print("Count of a:",count_a)


lst.insert(1,'x')
print(f"After insert:{lst}")

lst.remove('b')
print(f"After removal:{lst}")

lst.sort()
print(f"After Sort:{lst}")



# Question2: Write a Python program to count the number of strings where the string length is 2 or more and the
# first and last character are same from a given list of strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2


sample_list = ['abc', 'xyz', 'aba', '1221']
count=0


for string in sample_list:
    if(len(string)>=2 and string[0]==string[-1]):
        count +=1

print("Result:" ,count)


# Question3) Write a list comprehension which, from a list, generates a lowercased version of each string that has
# length greater than five.


sample_list2 = ["HELLO", "WORLD", "PYTHON", "PROGRAMMING", "EXAMPLES", "AI"]
print(sample_list2)
print("result:")
for s in sample_list2:
    if(len(s)>5):
        print(s.lower())



# Question4)Write a Python program to print a specified list after removing the 0th, 4th and 5th elements
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow',’Teapink’]
# Expected Output : ['Green', 'White', 'Black']

SampleList = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
SampleList.remove('Red')
SampleList.remove('Pink')
SampleList.remove('Yellow')
print("After Removing: ",SampleList)




