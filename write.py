import datetime


def update_dict(laptop_dict):
    #Updating the text file after buying or selling of laptop.
    with open("laptops.txt", "w") as f:
        for values in laptop_dict.values():
            f.write("{},{},{},{},{},{}\n".format(
                values[0], values[1], values[2], values[3], values[4], values[5]))


def generate_invoice(laptop_dict, laptops_bought):

    while True:
        print("\n")
        print("Please fill the details to complete the order: \n")

        # taking information from users to generate a invoice
        company_name = "Octave Laptop Store"
        distributor_name = input("Enter the name of the distributor: ")
        admin_name = input("Enter the name of the admin: ")
        time = datetime.datetime.now()
        date = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
        print("\n")
        invoice = f"{'='*80}\n"
        invoice += f"{company_name}".center(80) + "\n"
        invoice += f"{'='*80}\n"
        invoice += "Ordered to: ".ljust(20) + distributor_name + "\n"
        invoice += f"{'-'*80}\n"
        invoice += "Time of issue: ".ljust(20) + time.strftime("%d-%m-%Y-%H-%M-%S") + "\n"
        invoice += f"{'-'*80}\n"
        invoice += f"{'Product Details:':<20}\n"
        invoice += f"{'-'*80}\n"
        invoice += "S.N".center(10) + "|" + "Product Name".center(20) + "|" + "Brand".center(15) + "|" + "Price($)".center(15) + "|" + "Quantity".center(15) + "|\n"
        invoice += f"{'-'*80}\n"

        total = 0
        for i, (id, quantity) in enumerate(laptops_bought.items(), start=1):
            product_name = laptop_dict[id][0]
            brand = laptop_dict[id][1]
            price = laptop_dict[id][2]
            total_price = int(price) * int(quantity)
            total += total_price
            invoice += str(i).center(10) + "|" + product_name.center(20) + "|" + brand.center(15) + "|" + str(price).center(15) + "|" + str(quantity).center(15) +  "|"+"\n"
            invoice += f"{'-'*80}" + "\n"
        invoice += "Total:".ljust(65) + "$".ljust(3) + f"{total:>7,.2f}\n"
        invoice += f"{'-'*80}\n"
        VAT = 0.13*total
        invoice += "VAT:".ljust(65) + "$".ljust(3) + f"{VAT:>7,.2f}\n"
        invoice += f"{'-'*80}\n"
        invoice += "Grand Total:".ljust(65) + "$".ljust(3) + f"{total+VAT:>7,.2f}\n"
        invoice += f"{'-'*80}\n"
        invoice += f"Order has been purchased from {distributor_name} by {admin_name}\n".ljust(20)
        invoice += f"{'='*80}\n\n" 

        with open(f"{distributor_name}_{date}.txt", "w") as f:
            f.write(invoice)

        print(invoice)

        break


def generate_bill(laptop_dict, laptops_sold):
    while True:
        print("\n")
        print("Please fill the following details to generate a bill:"+"\n")
        
        name = input("Enter the name of customer: ")
        address = input("Enter their address: ")
        phone = input("Enter their phone number: ")
        admin = input("Enter the name of the admin:")
        time = datetime.datetime.now()
        print("\n")
        # generating a bill and also creating a text file with name_datetime as the file name
        date = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")


        bill = '=' * 95 + "\n"
        bill += "Octave Laptop Store".center(85) + "\n"
        bill += '=' * 95 + "\n\n"
        bill += "Name:".ljust(20) + name + "\n"
        bill += "Address:".ljust(20) + address + "\n"
        bill += "Phone:".ljust(20) + str(phone) + "\n"
        bill += "Admin:".ljust(20) + admin + "\n"
        bill += "Time of Purchase:".ljust(20) + str(time) + "\n\n"
        bill += '-' * 95 + "\n"
        bill += f"Bill has been generated for {name} on {date}\n"
        bill += '-' * 95 + "\n"
        bill += "Products Details".center(80) + "\n"
        bill += '-' * 95 + "\n"
        bill += "S.N".center(10) + "|" + "Product Name".center(20) + "|" + "Brand".center(20) + "|" + "Price($)".center(20) + "|" + "Quantity".center(20) + "|\n"
        bill += '-' * 95 + "\n"
        total = 0
        shipping_cost = 500
        for i, (products_id, quantity) in enumerate(laptops_sold.items(), start=1):
            products_name = laptop_dict[products_id][0]
            brand = laptop_dict[products_id][1]
            product_price = laptop_dict[products_id][2]
            total_price = int(product_price) * int(quantity)
            total += total_price
            bill += str(i).center(10) +  "|" + products_name.center(20) + "|" + brand.center(20) + "|" + str(product_price).center(20) + "|" + str(quantity).center(20) + "|\n"
            bill += f"{'-'*95}\n"
        bill += "Total:".ljust(65) + "$".ljust(3) + f"{total:>7,.2f}\n"
        bill += '-' * 95 + "\n"
        bill += "Shipping Cost:".ljust(65) + "$".ljust(3) + f"{shipping_cost:>7,.2f}\n"
        bill += '-' * 95 + "\n"
        bill += "Grand Total:".ljust(65) + "$".ljust(3) + f"{total+shipping_cost:>7,.2f}\n"
        bill += '=' * 95 + "\n"
        bill += "Thank you for shopping with us!".center(80) + "\n"





        with open(f"{name}_{date}.txt", "w") as f:
            f.write(bill)
        print(bill)
        
        break

