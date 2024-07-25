def print_laptop(laptop_dict):
    # printing the data in a tabular format
    print("-"*107)  
    print("|","SN".center(5),"|","Product Name".center(20),"|","Brand".center(10),"|","Price($)".center(10), 
          "|","Quantity".center(10),"|","Processor".center(15),"|","GPU".center(15),"|")
    print("-"*107)  

    for key, value in laptop_dict.items():
        print("|",str(key).center(5),"|", str(value[0]).center(20),"|",str(value[1]).center(10), "|",
              str(value[2]).center(10), "|",str(value[3]).center(10), "|",str(value[4]).center(15), 
            "|",  str(value[5]).center(15), "|")
        print("-"*107) 
    
    return laptop_dict


def buy_laptops(laptop_dict):
    """
    This function takes in a dictionary of laptops and asks the user to enter the id and quantity of the laptop they want 
    to order. It then updates the dictionary with the quantity of laptops bought and returns a dictionary of laptops 
    bought with their respective ids and quantities.
    """
    laptops_bought = {}
    while True:
        while True:
            try:
                id = int(input("Enter the id of the laptop you want to order: "))
                while id <= 0 or id > len(laptop_dict):
                    raise ValueError
                break
            except (ValueError,TypeError):
                print("Please enter the valid ID")
                continue

        while True:
            try:
                quantity = int(
                input("Enter the quantity of the laptop you want to order: "))
                if quantity <= 0:
                    raise ValueError
                break
            except ValueError:
                print("The quantity you entered seems to be invalid. Please try again.")

                

        if id in laptops_bought:
            laptops_bought[id] += quantity

        else:
            laptops_bought[id] = quantity

        # Adding the quantity of laptops bought in the dictionary
        laptop_dict[id][3] = int(laptop_dict[id][3]) + int(quantity)

        
        while True:
            choice = input("Do you want to buy more laptops? (y/n): ").lower()
            if choice == "y":
                break
            elif choice == "n":
                return laptops_bought
            else:
                print("Invalid input. Please enter y or n.")


def sell_laptops(laptop_dict):
    """
    Function that allows the sale of laptops from a given dictionary.

    """
    laptops_sold = {}
    while True:
        while True:
            try:
                id = int(input("Enter the id of the laptop you want to sell: "))
                while id <= 0 or id > len(laptop_dict):
                    raise ValueError
                break
            except (ValueError,TypeError):
                print("Oops! You have entered a wrong ID. Please try again.")
                continue

        while True:
            try:
                quantity = int(
                input("Enter the quantity of the laptop you want to sell: "))
                if quantity <= 0:
                    raise ValueError
                break
            except ValueError:
                print("The quantity seems to be invalid. Please input a valid number.")
                

        if id in laptops_sold:
            laptops_sold[id] += quantity

        else:
            laptops_sold[id] = quantity

        # Adding the quantity of laptops sold in the dictionary
        laptop_dict[id][3] = int(laptop_dict[id][3]) - int(quantity)

        while True:
            choice = input("Do you want to sell more laptops? (y/n): ").lower()
            if choice == "y":
                break
            elif choice == "n":
                return laptops_sold
            else:
                print("Invalid input. Please enter y or n.")
        




