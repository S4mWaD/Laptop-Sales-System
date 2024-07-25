import greetings
import read
import operations
import write
import datetime

greetings.company_header()
greetings.greeting()

# Asking the user to buy, sell or exit the interface
while True:

    print("Press 1 to display laptops")
    print("Press 2 to sell laptops")
    print("Press 3 to purchase laptops")
    print("Press 4 to exit")

    try:
        user_input = int(input("Enter your choice: "))
    except (ValueError, TypeError):
        print("Invalid input. Please enter a number between 1 and 4.")
        continue
    
    if (user_input == 1):
        print("\n")
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Here is the list of laptops which has been updated on {time}")
        laptop_dict = read.display_laptop()
        operations.print_laptop(laptop_dict)

    elif (user_input == 2):
        print("\n")
        laptop_dict = read.display_laptop()
        operations.print_laptop(laptop_dict)
        laptops_sold = operations.sell_laptops(laptop_dict)
        write.update_dict(laptop_dict)
        write.generate_bill(laptop_dict, laptops_sold)

    elif (user_input == 3):
        print("\n")
        laptop_dict = read.display_laptop()
        print_laptop = operations.print_laptop(laptop_dict)
        laptops_bought = operations.buy_laptops(laptop_dict)
        write.update_dict(laptop_dict)
        write.generate_invoice(laptop_dict, laptops_bought)

    elif (user_input == 4):
        print("Please wait, the system is closing.")
        print("\n\n")
        print("Thank you!")
        break

    else:
        print("Invalid input. Please enter a number between 1 and 4.")
        continue

