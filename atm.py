P="123456"
AB=500.00
b=input("PLEASE INSERT THE CARD('Y'/'N'): ")
if b == "N":
    print("insert card correctly")
else:
    while True:
        p=input("Enter Your Pin")
        if p != P:
            print("Enter Correct pin")
        break
        
    while True:
        print("1. WITHDRAW")
        print("2. DEPOSIT")
        print("3. CHECK BALANCE")
        print("4. PIN CHANGE")
        c=int(input("Enter ur choice"))
        if c == 1:
            while True:
                w=float(input("Enter amount to withdraw"))
                if w<=AB:
                    AB=AB-w
                    print("ACCOUNT BALANCE: ",AB)
                else:
                    print("Insufficient Ammount in Your Account")
                break
            
        elif c == 2:
            d=float(input("enter amount to deposit"))
            AB=AB+d
            print("ACCOUNT BALANCE: ",AB)
        elif c == 3:
            print("ACCOUNT BALANCE: ",AB)
        elif c == 4:
            np=input("Enter new pin")
            P=np
            print("ATM PIN Successfully Changed")
        
                   
                
        
        
