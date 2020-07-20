# Define a function with 'arbitrary numbers of arguments' method named as ‘spec_opr(*numbers)’ . 
# This function sums all of the arguments after a process. This process is even numbers should
# be divided by 2 and odd numbers should be multiplied with 3 first and then added to the total sum.
# Examples:
# spec_opr(3, 2, 6) should return 13,
# spec_opr() should return 301,
# spec_opr(93, 12, 5, 84, -22) should return 331

def spec_opr(*numbers):
   total = 0
   for i in numbers:
      if i % 2 == 0:
         
         total += i/2 
      
      else:
         
         total += i*3
   
   return int(total)      
        

print(spec_opr(3,6,2))
print(spec_opr(58, 53, 10, -10, -40, -28, 8, 34, 70, -16, 33))
print(spec_opr(93, 12, 5, 84, -22))      
      
