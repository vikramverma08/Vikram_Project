# inputting all the contacts
repository = {
    "ABHINAI": 9701246042,
    "ABHISHEK": 8332077922,
    "AJAY": 6232749827,
    "AKHIL": 8374598943,
    "BALA": 9010303739,
    "BHADRA": 9396161616,
    "BHANU": 7981819889,
    "BUNNY": 7815800244,
    "CHARAN": 8367532436,
    "DEEPAK": 8466062726,
    "DEVI": 8074009903,
    "DILEEP": 7993187395,
    "DIVYA": 9396961248,
    "GOWTHAM":9381156559,
    "RAHUL": 9492822397,
    "AUTHOSH": 7703842744,
    "RISHI": 6394542230,
    "THILUCK": 8885619995,
    "DIVYANSH": 6394834585,
    "KARTHIK": 9347773829,
    "SAUMYA": 7087717541,
    "HITHISH": 9494556505,
    "NAVEEN": 7981214473,
    "SUNIL": 6303141055,
    "VARDHAN": 6300930466,
    "SRINU": 9110529921,
    "RAJKUMAR": 9305839755,
    "VIVEK": 9392825262,
    "TANISHQ": 7584737373,
    "JAYAKRISHNA": 9391688677
}


# Searches the dictionary and prints the key value pair incase the key isn't present, it adds it to the dict and prints it''

def single_search():
    name = input("Enter the name of the contact you wish to search for: ").upper()
    if name in repository:
        print(f"\n{name}: {repository[name]}")
    else:
        b = input("\nNo such contact found\nIf you wish to add one, type 'Yes' else type 'No': ").lower()
        if b == "yes":
            new_contact(name)
            print(f"{name}: {repository[name]}")
        elif b == "no":
            pass
        else:
            print("Enter either yes or no ")


# Searches the dictionary and prints multiple key value pair and incase any key isn't present, it adds it to the dict and prints it along with the others.

def multiple_search():
    result = {}
    s1 = []
    s = 0
    name1 = input("Enter the names of the contacts seperated by commas: ").split(",")
    for i in name1:
        i = i.upper()
        if i in repository:
            result[i] = repository[i]
        else:
            s1.append(i)
            s += 1
    if s > 0:
        c = (input(f"\nCouldn't find contacts {s1}. \nDo you wish to add them? Enter Yes or No: ")).lower()
        if c == "yes":
            for i in s1:
                new_contact(i)
                if i in repository:
                    result[i] = repository[i]
            print()
            print(result)
        elif c == "no":
            print()
            if result == {}:
                pass
    else:
        print()
        print(result)


# adds new contact every time its called

def new_contact(contact_name):
    print()
    contact_number = int(input("Enter their contact number: "))
    repository[contact_name] = contact_number


choice = int(input(
    "Would you like to: \n\n1. Search for a single contact \n2. List all the contacts \n3. Search for multiple contacts \n \nEnter your choice: "))

if choice == 1:
    single_search()

elif choice == 2:
    print()
    print(repository)

elif choice == 3:
    multiple_search()

else:
    print("Choose from the given options!")

