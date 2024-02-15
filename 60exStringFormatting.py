kg=int(input("Enter the Quantity:"))
veg=input("Enter the Vegetable:")
price=int(input("Amount:"))
mypurchase="You have purchased {} kg of {} for {:.2f} Rupees."
print(mypurchase.format(kg,veg,price))