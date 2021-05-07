contacts={}
print("--------Contacts---------")
while True:
    print("\nSelect the operation")
    print("1.Insert the contact")
    print("2.Search for the contact")
    print("3.Delete the contact")
    print("4.Display all the contacts")
    print("5.delete all the contacts")
    print("6.edit the contact")
    print("7.Number of contacts")
    n=int(input("\nenter your choice"))
    if(n==1):
        contacts[input("\nenter the name")]=input("\nenter the numer")
        print(contacts)
    elif(n==2):
        name=input("\nenter name to search")
        for x,y in contacts.items():
            if(name==x):
                print("\nname=",x + "\ncontact=",y)
        
    elif(n==3):
        name = input("enter name to delete") 
        if name in contacts.keys():
            contacts.pop(name)
        else:
            print("Not Found\n")
        print(contacts)
    elif(n==4):
        print(contacts)
    elif(n==5):
        if(len(contacts)==0):
            print("the list is already empty")
        else:
            del contacts
        print(contacts)
    elif(n==6):
        print("\n 1.name changing")
        print("\n 2.number change")
        m=int(input("enter ur choice"))
        if(m==1):
            name=input("\nenter name to edit")
            newname=input("\nenter new name to edit")
            for x,y in contacts.items():
                if(name==x):
                    x=newname
                else:
                    print("\n Contact not found")
        if(m==2):
            name=input("\nenter name to edit")
            newnumber=input("\nenter new number to edit")
            for x,y in contacts.items():
                if(name==x):
                    y=newnumber
                else:
                    print("\n Contact not found")
        print(contacts)
    elif(n==7):
        print(len(contacts))
    else:
        break


    
