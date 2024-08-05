''' Task 3 catering choices. Ask the user if they want vegetarian food
Recommend "Veggie Delight Caterers if yes otherwise recommend "Gourmet Meals Caterers
'''
user = input("Do you want vegetarian food: yes or no? ") 
catering_choice = ""

if user == "yes":
    catering_choice = "Veggie Delight Caterers"
else:
    catering_choice = "Gourmet Meals Caterers"

print(f"Recommeded catering:  {catering_choice}")