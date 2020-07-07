#I didn't understand exactly what you wanted in this assignment
#so I did something like this.
print("""Are you over 75 years old?\nDo you have a severe chronic disease?
Is your immune system too weak?\n""")
age = not True #For me
chronic = False #For me
immune = False #For me

risk = age or chronic or immune
print(age,chronic,immune)
print(risk,"There is not a risk of death.", sep ="/" ,end="\n\n")

#Let's get the True output.
age = True
chronic = True
immune = False

risk = age and chronic or immune
print(age,chronic,immune)
print(risk,"There is a risk of death.",sep="/")