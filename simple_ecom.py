print("---Welcome to Online shopping nepal----")
print("1.Shoes(Rs3000),2.Handbag(Rs2000),3.MacbookM5(Rs197000)")
Shoes_price=0
Handbag_price=0
MacbookM5_price=0
product_name=""
quantity=0

option= int(input("Select an option: "))
if  option == 1:
   quantity= int(input("Enter the quantity you would like to purchase: "))
   Shoes_price= 3000*quantity
   product_name= "Shoes"
 

elif option == 2:

     quantity= int(input("Enter quantity for Handbag:"))
     Handbag_price= 2000*quantity
     product_name="Handbag"

elif option == 3:

     quantity= int(input("Enter quantity for MacbookM5:"))
     MacbookM5_price= 197000*quantity
     product_name="MacbookM5"


else:
    print("Invalid option selected.")




Receipt=Shoes_price + Handbag_price + MacbookM5_price
print("Your total receipt=", Receipt)


name = input("Enter your name: ")
phonenumber = int(input("Enter your phone number: "))
address = input("Enter your address: ")

print(product_name)
print(name)
print(phonenumber)
print(address)
 

exit()


  