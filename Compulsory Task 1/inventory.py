# Assumes reviewer has Tabulate module installed via pip install tabulate.
# Import modules used in code
import math
import string
from datetime import date
from tabulate import tabulate

# Define requestd class 
class Shoe:

    def __init__(self, 
                 country, 
                 code, 
                 product, 
                 cost, 
                 quantity):

        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
    # Requested class methods.
    def get_cost(self):
        """
        returns cost attr of 
        object as an integer
        """
        return int(self.cost)
    
    def get_quantity(self):
        """
        returns quantity attr of 
        object as an integer
        """
        return int(self.quantity)

    def __str__(self):
        """
        returns all attributes 
        printed as string
        """
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}"

def main():

    shoe_list = []
    
    # Requested function.
    def read_shoes_data():
        """
        Populates shoe list. Clears list on each call, to prevent multiple appends
        Reads lines from file, replaces \n with "," and splits on ","
        each prop now has index by which it can be assigned to attributes.
        I did not remove the first line of the txt file because it came in useful
        in later functions such as tabulate.
        """
        shoe_list.clear()
        with open('inventory.txt','r',encoding='utf-8') as f:
            for line in f:
                # Create comma delimited, str list with "\n" removed.
                shoe_props = (line.replace("\n",",").split(","))
                new_shoe = Shoe(shoe_props[0], 
                                shoe_props[1], 
                                shoe_props[2], 
                                shoe_props[3], 
                                shoe_props[4])

                shoe_list.append(new_shoe)

    # Requested function.
    def capture_shoes():
        """
        Prompts request input for attribute fields
        various methods of defensive programming
        ensure good data entry.
        shoe_list is appended line by line at end of fn.
        """
        countries = []
        with open('countries.txt', 'r',encoding='utf-8' ) as g:
            # Compares input with list of country names.
            for line in g:
                cntry = line.replace("\n","").strip()
                countries.append(cntry)
            country = input("\nPlease enter country.\n\n: ")
            # Capwords gives capitalisation of all component words
            country = string.capwords(country)
            while country not in countries:
                country = str(input("\nPlease enter a valid country.\n\n: "))
                country = string.capwords(country)
            print(f"\nYou have entered {country}.")

        with open('inventory.txt','r',encoding='utf-8') as f:
            # Compares input with existing object codes and while loop checks format.
            contents = f.read()
            code = input("\nPlease enter product code (e.g 'SKUxxxxx).\n\n: ").upper()
            while (code in contents or 
                    "SKU" not in code or 
                        len(code) != 8):

                code = input(
"""
You entered an already utilised
or invalid product code.
Please try again.

: """
                       ).upper()
            print(f"\nYou have entered {code}.")

        # Not much can be done defensively else to ensure name is double checked
        product = input("\nPlease enter a product name.\n\n: ")
        while True:
            confirm = input(
f"""
You have entered '{product}'.

Please CONFIRM product name.

: """
                      )
            if confirm.strip() == product.strip():
                break
            else:
                product = input(
"""
Product names do not match.

Please enter a product name.

: """
                          )
        print(f"\nProduct name'{product}' has been confirmed")

        while True:
            # Try/except ensures integer input type.
            try:
                cost = int(input(f"\nPlease enter product name '{product}' price.\n\n: "))
                confirm = int(input(
f"""
You have entered {cost}.

Please CONFIRM product name '{product}' price.

: """
                          ))
                # While double checks input.
                while confirm != cost:
                    confirm = int(input(
f"""
Product prices do not match.

Please CONFIRM product name {product} price.

: """
                              ))
                print(f"\nPrice: {cost}, has been confirmed")
                break

            except ValueError:
                print("\nYou have not entered a valid price.")

        while True:
            try:
                # Try/except ensures integer input type.
                quantity = int(input(f"\nPlease enter product name '{product}' quantity.\n\n: "))
                confirm = int(input(
f"""
You have entered {quantity}.

Please CONFIRM product name '{product}' quantity.

: """
                          ))
                # While double checks input.
                while confirm != quantity:
                    confirm = int(input(
f"""
Product quantities do not match.

Please CONFIRM product name {product} quantity.

: """
                              ))
                print(f"\nQuantity: {quantity}, has been confirmed\n\n")
                break

            except ValueError:
                print("\nYou have not entered a valid quantity.")
        # New object assembled with values input above.
        capt_shoe =  Shoe(country, 
                          code, 
                          product, 
                          cost, 
                          quantity)
        # Shoe_list is updated.
        shoe_list.append(capt_shoe)
        # Iventory.txt is updated
        with open('inventory.txt','w+',encoding='utf-8') as f:
            for obj in shoe_list:
                f.write(str(obj)+"\n")
        # Confirmation message of new capture.        
        print(
f"""
Product details:

{str(shoe_list[-1])}

have been added to the inventory
"""
        )
    # Requested function.
    def view_all():
        """
        View all iterively splits the attributes of an object,
        appending to a string list and tabulates the list 
        """
        prnt_obj = []
        # Append object properties as lists to list "prnt_obj"
        for i in range(len(shoe_list)):
            prnt_obj.append(str(shoe_list[i]).split(","))
        print(
"""
__________________________________________________________

******Current stock levels:******
__________________________________________________________

"""
        )
        # Create table of attr, using first line of shoe_list as header
        print(tabulate(prnt_obj,headers = 'firstrow',tablefmt='fancy_grid'))

    # Requested function.
    def re_stock(shoe_list, sku = "", i = 0, index = 1, low_stck = math.inf):
        """
        Recursively compares stock levels for the lowest value.
        variables are declared in the function arguments, and are carried through
        via the arguments to the next recursion.
        Options to increase stock levels are provided, and new levels are written to 
        Object,and txt file
        """
        if index == len(shoe_list):
            i = i
            sku = sku
        
        else: 
            # Low stock starts at infinity and lower values logged via "low_stck"
            if low_stck > int(shoe_list[index].quantity):
                low_stck = int(shoe_list[index].quantity)
                # Values for code and index associated with lowest stock are logged via "i" and "sku"
                sku = shoe_list[index].code
                i = index
            return re_stock(shoe_list, sku, i, index + 1, low_stck)
        # Intersting looking output
        print(
f"""
The stock system has detected you have low stock levels of:

Item name ................. {shoe_list[i].product}
Item code ................. {shoe_list[i].code}
Item quantity ............. {shoe_list[i].quantity}
"""
        )
        # Empty value q declared.
        q = 0
        while True:
            
            # Quantity options
            re_order = int(input(
"""
You may re-order in quantites of 5, 10 or 15 pieces.
Please select a quantity

: """
                    ))

            if re_order == 5:
                q = 5
                break

            elif re_order == 10:
                q = 10
                break

            elif re_order == 15:
                q = 15
                break

            else:
                print("\nYou have not selected a valid quantity.")

        print(f"\nYou have selected {q} pieces:\n") 

        # Var "q" added to current stock, converted to string and written to txt file and obj
        shoe_list[i].quantity = str(int(shoe_list[i].quantity) + q)
        with open('inventory.txt','w+',encoding='utf-8') as f:
            for obj in shoe_list:
                f.write(str(obj)+"\n")
        print("\nStock has been updated\n")
        view_all()

    # Requested function.
    def search_shoe():
        """
        Function checks format of entered code, then checks it
        exists in the inventory. if it does, the result is tabulated
        and presented.
        """
        # Checks input format.
        sku = input("\nPlease enter product code (e.g 'SKUxxxxx).\n\n: ").upper()
        while ("SKU" not in sku or 
                len(sku) != 8):
            sku = input(
"""
You entered an invalid product code.
Please try again.

: """
                    ).upper()
        prnt_obj = []
        # Checks input exists in inventory, appends to list and tabulates.
        count = 0
        for obj in range(len(shoe_list)):
            if sku == getattr(shoe_list[obj], "code"):
                count += 1
                prnt_obj.append(str(shoe_list[0]).split(","))
                prnt_obj.append(str(shoe_list[obj]).split(","))
        if count > 0:
            print(
f"""
__________________________________________________________

Information for item code: {sku}
__________________________________________________________

"""
            )
            print(tabulate(prnt_obj,headers = 'firstrow',tablefmt='fancy_grid'))
        else:
            print("\nThis code does not exist in inventory")


    # Requested function.        
    def value_per_item():
        """
        function uses class methods get_cost and get_quantity
        to calculate total invetory values per item and present
        as a table
        """
        # object declared to which we append list of objects props
        prnt_obj = []
        # First line of shoe_list appended for headers
        prnt_obj.append(str(shoe_list[0]).split(","))
        # Extra item "Total stock Value" added to header list
        prnt_obj[0].append("Total stock value")
        for obj in range(1, len(shoe_list)):
            # Rest of object properties appended to list
            prnt_obj.append(str(shoe_list[obj]).split(","))
        for item in range(1, len(prnt_obj)):
            # Total value calculated by object and apppended to each objects respective list
            price = shoe_list[item].get_cost()
            quant = shoe_list[item].get_quantity()
            prnt_obj[item].append(str(price * quant))
        
        # Results tabulated.
        print(tabulate(prnt_obj,headers = 'firstrow',tablefmt='fancy_grid'))

    def highest_qty(shoe_list, sku = "", i = 0, index = 1, most_stck = 0):
        """
        Recursively compares stock levels for the highest value.
        variables are declared in the function arguments, and are carried through
        via the arguments to the next recursion.
        Options to increase stock levels are provided, and new levels are written to 
        Object,and txt file
        """
        if index == len(shoe_list):
            i = i
            sku = sku
        
        else:
            # Most_stock starts at 0 and higher values logged via "most_stck"
            if most_stck < int(shoe_list[index].quantity):
                most_stck = int(shoe_list[index].quantity)
                # Values for code and index associated with lowest stock are logged via "i" and "sku"
                sku = shoe_list[index].code
                i = index
            return highest_qty(shoe_list, sku, i, index + 1, most_stck)
        # Intersting looking output
        curr_date = date.today()
        print(
f"""
The stock system has detected you have high stock levels of:

Item name ................. {shoe_list[i].product}
Item code ................. {shoe_list[i].code}
Item quantity ............. {shoe_list[i].quantity}

in:

Item country .............. {shoe_list[i].country}
"""
        )
        print(
f"""
The following notification has been automatically sent to:

Nike {shoe_list[i].country}

_______________________________________________

******************NOW ON SALE******************

Nike {shoe_list[i].product} at 35% off!!!!!!!

Original price .......................... R{shoe_list[i].get_cost()}
Reduced to .............................. R{shoe_list[i].get_cost() * 0.65}

Offer lasts one week from {curr_date.strftime('%d %b %Y')}
_______________________________________________

"""
        )
    # While True Menu options:
    while True:
        main_menu = input(
"""
Welcome to the provisional Nike footwear global stock system
would you like to:

a - Enter new footwear line?
b - View all currently in stock footwear lines?
c - Automatically search for and re-stock low inventory levels?
d - Automatically search and send offer notification for high inventory levels?
e - Search for and display details of specific footwear model
f - Display current stock capital per footwear line?
g - Exit?

: """
                    )
        # Applies to all. Read_shoes called often to ensure Shoe_list is kept up to date.
        # View all is called after any changes to txt file or shoe_list
        if main_menu == "a":
            read_shoes_data()
            capture_shoes()
            read_shoes_data()
            view_all()

        elif main_menu == "b":
            read_shoes_data()
            view_all()

        elif main_menu == "c":
            read_shoes_data()
            re_stock(shoe_list)
            read_shoes_data()
            view_all()
        
        elif main_menu == "d":
            read_shoes_data()
            highest_qty(shoe_list)

        elif main_menu == "e":
            read_shoes_data()
            search_shoe()

        elif main_menu == "f":
            read_shoes_data()
            value_per_item()

        elif main_menu == "g":
            print("\nGoodbye!")
            exit()

        else:
            print("\nYou have made an invalid selection\n")

main()

# *****Notes***** 
# Code has been commented and functions have been documented per previous reviewers suggestion>
