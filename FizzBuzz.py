#Print numbers from 1 to 100 inclusively following these instructions
#if a number is multiple of 3, print "Fizz" instead of this number,
#if a number is multiple of 5, print "Buzz" instead of this number,
#for numbers that are multiples of both 3 and 5, print "FizzBuzz",
#print the rest of the numbers unchanged.

for i in range(1,101):
   if i % 3 == 0 and i % 5 == 0:
      print("FizzBuzz")
   elif i % 5 == 0:
      print("Buzz")
   
   elif i % 3 == 0 :
      print("Fizz")
   
   else:
      print(i)  
            
      
