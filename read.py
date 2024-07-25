def display_laptop():
    # Reading from the text file and storing it in a dictionary.
    laptop_dict = {}
    with open("laptops.txt","r") as f:
        SN = 1
        for line in f:
            line = line.replace("\n","")
            laptop_dict.update({SN: line.strip().split(",")})
            SN += 1
    
    return laptop_dict






