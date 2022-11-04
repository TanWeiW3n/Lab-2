print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67,32)")

def get_user_input():
    userNumbers = input("Enter your numbers:")
    newNumbers = userNumbers.split(",")

    list_of_floats = []

    #Changing inputs from string to float
    for item in newNumbers:
        list_of_floats.append(float(item))
    return list_of_floats


def main():
    display_main_menu()
    print(get_user_input())

if __name__ == "__main__":
    main()


