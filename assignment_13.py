a = 1
b = 1

my_list = [a,b]

for i in range(8):
   
   a,b = b,a +b
   my_list.append(b)
   

print(my_list)       