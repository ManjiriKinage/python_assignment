n= int(input("enter the number of element : "))
arr=[]
print("enter elements : ")
for i in range (n):
    arr.append(int(input()))
key = int(input("enter number to search : "))

found = False

for i in range(n):
    if arr[i] == key :
        print("value found at position : ",i )
        found =True
        break
if not found :
    print("value not found")