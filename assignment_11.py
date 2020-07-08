number = input("Please enter a number: ")
sum = 0
while not number.isdecimal():
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
    number = input("Please enter a number: ")
if number.isdecimal():
    for i in range(len(number)):
         sum += int(number[i])**len(number)
    if  sum == int(number):
         print("{} is an Armstrong number".format(int(number)))
    else:
        print("{} is not an Armstrong number".format(int(number)))




"""number = input("Please enter a positive number: ")
sum = 0

while not number.isdecimal():
   print("It is an invalid entry. Dont use non-numeric,float or negative values.")
   number = input("Please enter a positive number:")
   

if number.isdecimal():
   for i in range(len(number)):
      sum += int(number[i])**len(number)
      if sum == int(number):
         print(f"{(int(number))} is a Armstrong number.")
      else:
         print(f"{(int(number))} is not an Armstrong number.")    """  
      

