number = input("Please enter a positive number: ")
basamak_sayısı = len(number)

number = int(number)

basamak = 0
toplam = 0

gecici_number = number

while gecici_number > 0:
    basamak = gecici_number % 10 
    toplam += basamak ** basamak_sayısı
    
    gecici_number //= 10  
     
if (toplam == number):
   print(f"{number} is an armstrong number.")     

else:
   if (number <= 0):
      print("Please enter a positive number.")   
   elif number == type(str):
      print("Dont use any entries ")
   
   elif number == float(number):
      print("Please enter an integer number.")                
                   