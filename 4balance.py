balance=0
MIN_BALANCE=500
 
print("enter transaction  ( example: D 300 or W 200 )")
print("Type END to stop\n")

while True :
    entry = input("enter transaction : ")
    
    if entry.upper() == "END":
        break
    
    t_type ,amount =entry.split()
    amount= int(amount)
    
    if t_type == 'D' :
        balance += amount
        print("Deposited:", amount)
        
    elif t_type =='W':
        if balance- amount < MIN_BALANCE:
            print("Withdrawal denied! Minimum balance must be 500")
        else :
            balance -= amount
            print("Withdrawn:", amount)
    else:
        print("Invalid transaction")
    
    print("Current Balance =", balance)
    print("----------------------")
        
print("\nNet Account Balance =", balance)

        