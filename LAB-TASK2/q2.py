# (II)In a company ,worker efficiency is determined on the basis of the time required for a worker
# to complete a particular job.If the time taken by the worker is between 2-3 hours then the worker
# is said to be highly efficient. If the time required by the worker is between 3-4hours,then the worker
# is ordered to improve speed. If the time taken is between 4-5 hours ,the worker is given training to
# improve his speed ,and if the time taken by the worker is more than 5 hours ,then the worker haas
# to leave the company, If the time taken by the worker is input through the keyboard,find the
# efficiency of the worker


time=float(input("Enter Time Taken BY Worker (in Hrs): "))
if 2<=time<3:
    print("Highy EFficient") 
elif 3<=time<4:
    print("Improve Speed")
elif 4<=time<5:
    print("Training Shoud be given")
else:
    print("Worker Has to Leave")