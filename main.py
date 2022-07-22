import time
ts = time.localtime()
print(time.strftime("%Y-%m-%d %H:%M:%S", ts))

while True:

     print("\n**********Welcome to Pizza Palace - Demo***********")
     print("1.  Display Orders")
     print("2.  Add New Order")
     print("3.  Remove Order")
     print("4.  Edit Order")
     print("5.  Save Order")
     print("6.  Exit Program")
     menu_option = input("Select an option:")

     if (menu_option == "2"):
         add_new_number = input("Enter your order number:")
         add_new_type = input("Enter your order type:")
         add_new_amount = input("Enter your order amount:")
         print(add_new_number, "has been added")

     elif (menu_option == "3"):
         edit = input("Enter order number to remove:")
         edit.clear()
         print("Removed")

     elif (menu_option == "4"):
         new_order_edit = input("Which order would you like to edit?")
         new_number_edit = input("Enter new order number:")
         new_type_edit = input("Enter new order type:")
         new_amount_edit = input("Enter new amount:")
         print(new_order_edit, "has been changed to:", new_number_edit)
         
     elif (menu_option == "1"):
         print(f"\n********Order List ** \nOrder Number:{new_number_edit} "
               f"\nOrder Type:{new_type_edit} \nOrder Amount:{new_amount_edit} \n--------- \n********")

     elif (menu_option == "5"):
         order = new_number_edit, new_type_edit, new_amount_edit
         file_name = input("Enter file name:")
         file = open('order.txt', 'w')
         file.write(repr(order))
         print("Saving....")
         file.close()
         print("Data Saved")
     elif (menu_option == "9"):
         exit()


         continue






















