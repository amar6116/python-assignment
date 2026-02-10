m=int(input("enter no of student marks"))

marks=[0]*m
valid=0
fail=0
for i in range(m):
    marks[i] = int(input(f"Enter mark for student {i+1}:"))
name="amar"
for i in range(m):
    if len(name)>6:
        marks[i]=marks[i]+2
    else:
        marks[i]=marks[i]-2


for i in range(m):
    if(marks[i]<=100 and marks[i]>90):
        print(marks[i],"-> Excellent")
        valid+=1
    elif(marks[i]<=89 and marks[i]>75):
        print(marks[i],"-> Very Good")
        valid+=1
    elif(marks[i]<=74 and marks[i]>60):
        print(marks[i],"-> Good")
        valid+=1
    elif(marks[i]<=59 and marks[i]>40):
        print(marks[i],"-> Average")
        valid+=1
    elif(marks[i]<=39 and marks[i]>=0):
        print(marks[i],"-> Fail")
        valid+=1
        fail+=1
    else:
        print(marks[i],"-> Invalid")



print("Total Valid students",valid)
print("Total failed students",fail)