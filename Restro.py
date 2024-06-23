menu={'Pav-Bhaji':60, 'Cold coffee':70, 'Golgappe':50, 'Rasgulla':15,'Ice-cream':50}

print("Welcome to My Restaurant")
print("Pav-Bhaji: Rs60\nCold coffee: Rs 70\nGolgappe: Rs 50\nRasgulla:Rs 15\nIce-cream: Rs50")
total_bill=0
order_1=input("What you would like to have:")
if order_1 in menu:
    total_bill += menu[order_1]
    print("Your ordered item added in the list!!")
else:
    print(f"The ordered item{order_1} is not available ")

order_2=input("Do you want to add another item? (Yes/No)")
if order_2=="Yes":
    item_2=input("Enter the another item:")
    if item_2 in menu:
        total_bill += menu[item_2]
        print("Your ordered item added in the list..")
    else:
        print(f"{item_2} is not available right now!")

print(f"Total bill you have to pay = {total_bill}")
print("THANK YOU SIR/MAM")
