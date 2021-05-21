def validate_input():
    while True:
        try:
            userInput = int(input("Enter a year: "))
        except ValueError:
            print("That is not an integer! Please try again")
            continue
        else:
            if(userInput <= 0):
                print("Enter a year that is greater than zero")
            else:
                break

    is_leap_year(userInput)



def is_leap_year(year):
    if(year % 4 == 0):
        if(year % 100 == 0):
            if(year % 400 == 0):
                return "{0} is a leap year!".format(year)
            else:
                return "{0} is not a leap year!".format(year)
        else:
            return "{0} is a leap year!".format(year)
    else:
        return "{0} is not a leap year!".format(year)