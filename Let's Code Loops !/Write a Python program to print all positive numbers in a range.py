list1 = [12, -7, 5, 64, -14]
print("Input:", list1)
print("Output:",end=" ")
for x in list1:
    if(x>0):
        print(x,end=",")

list2 = [12, 14, -95, 3]
print("\nInput:", list2)
positive=[]
for x in list1:
    if(x>0):
        positive.append(x)
print("Output:",positive)