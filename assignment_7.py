left = set("qwertasdfgzxcvb")
right = set("yuiophjklnm") # I didn't use Turkish character. 
word = set(input("Please enter your word: ")) #If you use Turkish character,the output'll True.

union_1 = (left.union(word))  
union_2 = (right.union(word))

left_hand = (len(union_1) > len(left))   #True or False
right_hand = (len(union_2) > len(right))
output = (left_hand and right_hand)

print(output)

