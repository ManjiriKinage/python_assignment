library=[]
def add_books(n):
    for i in range(n):
        name= input("Enter book name: ")
        cost=int (input("enter cost :"))
        library.append([name,cost])
def display():
    n=len(library)  
    for i in range(n):
        for j in range(0,n-i-1):
            if library[j][1]>library[j+1][1]:
                library[j][1],library[j+1][1] = library[j+1][1],library[j][1]
    print("\nBooks in ascending order of cost:")
    for book in library:
        print(book)           
        
def count():
    c=0
    for book in library :
        if book[1]==500:
            c += 1
    print("Number of books with cost 500 =", c)
        
def delete_duplicates():
    unique =[]    
    for book in library:
        if book not in unique :
            unique.append(book)
    library.clear() 
    library.extend(unique)
    print("duplicates removed ")
        

# -------- Main Program --------

n= int (input("enter number of books : "))
add_books(n)

while True :
    print("\n--- LIBRARY MENU ---")
    print("1. Delete duplicate entries")
    print("2. Display books in ascending order of cost")
    print("3. Count books with cost 500")
    print("0. Exit")
    
    ch= input("enter choice : ")
    if ch== '1':
        delete_duplicates()
    elif ch=='2' :
        display()
    elif ch=='3':
        count()
    elif ch=='0':
        print("program ended")
        break
    else:
        print("invalid choice")