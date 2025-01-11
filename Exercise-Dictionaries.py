#Exploring dictionaries and try some functions 
#Question 1)
sample_dict={'a':1,'b':2,'c':3}
print("Values: ",sample_dict.values())
print("Keys: ",sample_dict.keys())
print(sample_dict.get('b'))
sample_dict['d']=4
print("After Adding: ",sample_dict)
remove_value=sample_dict.pop('b')
print("After Popping: ",sample_dict)
sample_dict.update({'e':5,'f':6})
print("After Updating: ",sample_dict)
sample_dict.clear()
print("After Clearing: ",sample_dict)

#Question 2)
# Write a Python script to concatenate following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

dic1.update(dic2)
dic1.update(dic3)
print("Resukt: ",dic1)

