import fontstyle
text = fontstyle.apply('Welcome to the Ocean Cafe Website!', 'bold/Italic')
t = fontstyle.apply('MENU', 'bold')
print(text)

print("\n\n",t)
print("\n Drinks \t\t\t\t\t Desserts/Snacks")
print("\n Latte \t AED 25 \t\t\t Fruit Tart \t AED 5")
print("\n Hot Cocoa \t AED 10 \t\t Cheesecake \t AED 15")
print("\n Iced Tea \t AED 20 \t\t Panna Cotta \t AED 15")
print("\n Mocha \t AED 25 \t\t\t Ice Cream \t\t AED 5")
print("\n Cappuccino or \n Frappuccino \t AED 25 \t Chocolate \t\t AED 7")

product = {"latte": 25, "fruit tart": 5, "hot cocoa": 10, "cheesecake": 10, "iced tea": 20, "panna cotta": 15, "mocha": 25, "ice cream": 5, "cappuccino": 25, "frappuccino": 25, "chocolate": 7}

print("\nProduct     Quantity     Price/unit($)     Total price")
total = 0
def search():
    global total
    item = input(" ")
    item = item.lower()
    if item in product:
        quan = int(input("\t\t\t\t"))
        print('\t\t\t\t\t\t\t', product[item], "\t\t\t\t" ,quan * product[item])
        total = total + quan * product[item]
    elif item == 'end':
        print("--------------------------------------------------------------")
        print("                          Grand Total           ", total)
        exit()
        print("\n\n\n Thanks for ordering from the Ocean Cafe! Enjoy!")
    else:
        print("Invalid Item")



while True:
    search()