# Count the number of each letter in a sentence.
# The department you work for undertook a project construction that makes word / text analysis. 
# You are asked to calculate the number of letters or any chars in the sentences entered under this project.
# Write a Python program that;
# takes a sentence from the user,
# counts the number of each letter of the sentence,
# collects the letters/chars as a key and the counted numbers as a value in a dictionary.

        
sentence = input("Please enter a sentence: ")

dic = {}
for i in sentence:
   dic[i] = dic.get(i,0)+1

print(dic)
 





#TEST  

"""sentence = input("Please enter a sentence: ")
lis = {}

for i in sentence:
   c = sentence.count(i)
   lis["i"] = c
      
print(lis)"""

"""sentence = input("Please enter a sentence: ")
harf=[]
count =[]

for i in(sentence):
    if not (i in harf):
        harf.append(i)
        count.append(1)
    
for j in range(len(harf)):
    print(harf[j], count[j])
    
    
#else:
        #sayi[harf.index(i)]=sayi[harf.index(i)]+1 """
        
