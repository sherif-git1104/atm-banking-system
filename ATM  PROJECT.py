account={}
next_acc_no=2000
while True:
    print("\n......ATM MENU......")
    print("1.create account")
    print("2.delete account")
    print("3.login")
    print("4.exit")
    
    main_choice=int(input("enter choice:"))
    if main_choice==1:
        name=input("enter name:")
        pin=int(input("create 4-digit  pin:"))
        balance=int(input("enter initial balance:"))

        acc_no=next_acc_no
        account[acc_no]={
            "name":name,
            "pin":pin,
            "balance":balance,
        }
        next_acc_no=next_acc_no+1
        print("account created sucessfully")
        print("your account nimber is:",acc_no)
    elif main_choice==2:
        acc_no=int(input("enter account number: "))
        pin=int(input("enter pin:"))
        if acc_no in account and account[acc_no]["pin"]==pin:
            del account[acc_no]
            print("account deleted sucessfully")
        else:
            print("invalid account number or pin")
    elif main_choice==3:
        acc_no=int(input("enter account number:"))
        attemts=3
        if acc_no in account:
            while attemts>0:
                pin=int(input("enter pin:"))
                if pin==account[acc_no]["pin"]:
                    print("welcome ,",account[acc_no]["name"])

                    while True:
                        print("/n.....ATM OPERATION......")
                        print("1.check balance")
                        print("2.deposit")
                        print("3. ammount withdraw")
                        print("4.logout")

                        choice=int(input("enter choice:"))
                        if choice==1:
                            print("balance",account[acc_no]["balance"])
                        
                        elif choice==2:
                            amount=int(input("enter amount:"))
                            account[acc_no]["balance"]=account[acc_no]["balance"]+amount
                            print("updated balane,",account[acc_no]["balance"])
                        
                        elif choice==3:
                            
                            amount=int(input("enter amount withdraw:"))
                            if amount>=account[acc_no]["balance"]:
                             account[acc_no]["balance"]=account[acc_no]["balance"]-amount
                             print("remaining balnce,",account[acc_no]["balance"])
                            else:
                                print("insufficent balance")
                        elif choice==4:
                            print(" logout sucessfully")
                            break
                        else:
                            print("invalid operation")
                    break
                
                else:
                    attemts=attemts-1
                    print("wrong pin")
                    if attemts==0:
                        print("card blocked")
                    else:
                        print("attempts left:",attemts)
            else:
                print("account not found")
    elif main_choice==4:
        print("thank you for using atm")
        break
else:
    print("invalid choice")



