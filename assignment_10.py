age = input("Are you a cigarette addict older than 75 years old?: ").title() == "Yes"
chronic = input("Do you have a severe chronic disease?: ").title() == "Yes"
immune = input("Is your immune system too weak?: ").title() == "Yes"


risk = age or chronic or immune

if risk == True:
   print("You are in risky")
   
else:
   print("You are not in risky group")