'''
WAP that has following menu:
- Enter code w for withdraw
- Enter code d for deposit
- Enter code c for checking balance

Note: You can withdraw an amount only if balance is geater than or equal to 500 and withdrawing balance should be less than balance.
'''
ac_bal = 5000
choice = input("Enter code w for withdraw\nEnter code d for deposit\nEnter code c for checking balance\n\nPlease enter your choice: ").lower()

if choice == "w":
    wd_amt = int(input("\nPlease enter the amount you wish to withdraw: "))
    if wd_amt > ac_bal or ac_bal < 500:
        print("\nSorry! this request can't be prcessed because of insufficient balance")
    else:
        ac_bal = ac_bal - wd_amt
        print("\nYour request has been processed.\nAvailable balance: ", ac_bal)

elif choice == "d":
    dep = int(input("Please enter the amount you wish to deposit: "))
    print("\nYour account's previous available balance was: ", ac_bal)
    ac_bal = ac_bal + dep
    print("Your account's new available balance is: ", ac_bal)

elif choice == "c":
    print("Your account's available balance is: ", ac_bal)
