import datetime


def company_header():
    comp_name = "---------------------------------------------------------------------------------------------------------------------------------------------------------\n"
    comp_name += "                                                                OCTAVE LAPTOP STORE                                                      \n"
    comp_name += "                                                                  Kathmandu, Nepal                                                       \n"
    comp_name += "                                                   Phone: 01-5452522 | Email: info@octavelaptopstore.com                                 \n"
    comp_name += "---------------------------------------------------------------------------------------------------------------------------------------------------------\n"
    print(comp_name)

    return comp_name


def greeting():
    time = datetime.datetime.now().hour
    if time < 12:
        print("Good Morning Admin!")
        print("\tPlease choose a suitable option so that we can help you.")
    elif time < 18:
        print("Good Afternoon Admin!")
        print("\tPlease choose a suitable option so that we can help you.")
    else:
        print("Good Evening Admin!")
        print("\tPlease choose a suitable option so that we can help you.")





