my_name = "Orhan"
my_password = "O@R13"
first_name = input("Please enter your first name: ").title().strip()
if my_name == first_name:
    print(f"Hello,{my_name}!. The password is : {my_password}")
else:
    print(f"Hello, {first_name}! See you later.")   
   
   