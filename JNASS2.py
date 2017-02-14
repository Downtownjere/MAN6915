#problem 1. Prompt user to enter order amount and state. If state is WI add 5.5% state tax. Return total


def problemone():
    orderamount = int(input("What is the order amount?"))
    state = input("What is the state?")
    tax = 0


    if state == 'WI' or state == 'wi' or state =='Wi' or state == 'wI':
        tax = orderamount * 0.055 + 0.005
        print("The subtotal is: ${0:.2f}".format(orderamount))
        print("The tax is: ${0:.2f}".format(tax))

    total = round(orderamount + tax , 2)
    print("The total is ${}".format(total))


#Problem 2. Program to validate user input against a known password value

def problemtwo():
    password = input("what is the password: ")
    systempassword = 'abc$123'

    if password == systempassword:
        print("Welcome!")
    else:
        print("I don't know you.")


#Problem 3. Takes in user inputed age and validates it against the legal driving age

def problemthree():
    legalage = 16
    userage = int(input("What is your age?"))
    variable = ""

    if userage >= legalage:
        variable = ""
    else:
        variable = "not "

    print("You are {}old enough to legally drive".format(variable))


#Problem 4. Calculate the users Blood Alochol Content

def problemfour():
    try:
        gender = int(input("What is your gender? Enter 1 for Male, 0 for Female"))
        weight = int(input("What is your weight?"))
        drinks = int(input("How many drinks have you had?"))
        volume = int(input("What is the alcohol by volume?"))
        time = int(input("When was your last drink(in hours)"))
    except ValueError as e:
        print("You have entered an incorrect value. ")

    total_alcohol = drinks * volume
    if gender == 1:
        ratio = 0.73
    else:
        ratio = 0.66

    bac = (total_alcohol * 5.14 / weight * ratio) - 0.015 * time
    if bac >= 0.08:
        variable = "not "
    else:
        variable = ""
    print("Your BAC is {}".format(bac))
    print("It is {}legal for you to drive".format(variable))



#Problem 5. Convert a temperature into either Celcius or Fahrenhieght depending what was entered

def problemfive():
    print("Press C to convert from Fahrenheit to Celsius.", "\n"
    "Press F to convert from Celsius to Fahrenheit")
    degree = input()
    degree = degree.upper()
    temperature = ""
    convert = ""
    print("Your choice:", degree)

    if degree == 'C':
        tempfah = int(input("Please enter the temperature in Fahrenheit"))
        temperature = 'Celcius'
        convert = (tempfah - 32) * 5/9
    elif degree == 'F':
        tempc = int(input("Please enter the temperature in Celcius"))
        temperature = 'Fahrenheit'
        convert = (tempc * 9 / 5) + 32
    else:
        print("You did not enter C or F")
        pass

    print("The temperature in {} is {}".format(temperature, convert))



#Problem 6. Calculate BMI from user height/weight input
def problemsix():
    try:
        weight = int(input("How much do you weigh?"))
        height = int(input("How tall are you in inches?"))
    except ValueError as e:
        print("You have entered an incorrect value. ")

    bmi = (weight/(height **2)) * 703
    if 18.5 <= bmi <= 25:
        print("Your BMI is {}".format(bmi))
        print("You are within the ideal weight range.")
    elif bmi < 18.5:
        print("Your BMI is {}".format(bmi))
        print("You are underweight. You should see a doctor")
    else:
        print("Your BMI is {}".format(bmi))
        print("You are overweight. You should see your doctr")



#Problem 7.Calculate tax, including state/county
def problemseven():
    order_amt = int(input("What is the order amount? "))
    state = input("What state do you live in (use abbreviation)? ")
    county = input("What county do you live in? ")
    state = state.upper()
    county = county.upper()
    tax = 0
    total = order_amt + tax


    if state == 'WI' and county == 'EAU CLAIRE':
        tax = order_amt * (0.05 + 0.005)
    elif state == 'WI' and county == 'DUNN':
        tax = order_amt * (0.05 + 0.004)
    elif state == 'IL':
        tax = order_amt * 0.08
    else:
        tax = 0

    print("The tax is ${}. \nThe total is ${}.".format(tax, total))


#Problem 8. Write a program that converts a number from 1 to 12 to the corresponding month.

def problemeight():
    month = int(input("Please enter the number of the month: "))
    month_convert = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
                     9: 'September', 10: 'October', 11: 'November', 12: 'December'}

    if 0 < month <=12:
        print('The name of the month is {}'.format(month_convert[month]))
    else:
        print("You entereted an incorrect month, please try again")
        problemeight()


#Problem 9.
def problemnine():
    from collections import Counter
    print("Enter two strings and I'll tell you if they are anagrams:")
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")
    string1_length = len(string1)
    string2_length = len(string2)

#this function uses the Counter module from the collections library. The counter module uses .....
#for the Counter test, I decided to use the .upper() function call so in case the user types a letter in caps in one
#word but not the other, it will still provide the correct

    def isAnagram(string1, string2):
        return Counter(string1.upper()) == Counter(string2.upper())

    if isAnagram(string1, string2) == 1 and string1_length == string2_length:
        print('"{}" and "{}" are anagrams'.format(string1, string2))
    else:
        print('"{}" and "{}" are not anagrams'.format(string1, string2))


#problem 10. Create a program to determine the complexit of a given password.

def problemten():
    password = input("What is your password: ")
    password_test = ''

    def hasNumbers(x):
        return any(char.isdigit() for char in x)

    def specialchar(x):
        valid = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')
        return set(x).issubset(valid)


    def passwordValidator(x):
        if str.isdigit(x) and len(x) < 8:
            return 'very weak'
        elif str.isalpha(x) and len(x) < 8:
            return 'weak'
        elif hasNumbers(x) and specialchar(x) and len(x) >= 8:
            return 'strong'
        else:
            return 'very strong'

    password_test = passwordValidator(password)

    print("The password {} is a {} password.".format(password, password_test))


#problem 11. Write a program to determine the length of time it will take to pay off a credit card.
def problemeleven():
    import math
    balance = float(input("What is your balance? "))
    apr = float(input("What is the APR on the card? "))
    payment = float(input("What is the monthly payment you can make? "))
    daily_apr = apr / 365 / 100

    def calculateMonthsUntilPaidOff(balance,payment,daily_apr):
        log_test2 = 1 + balance / payment * (1 - (1 + daily_apr) ** 30)
        log_division = math.log(log_test2) / math.log((1 + daily_apr))
        final_answer = round((-1/30) * log_division + 0.5)
        return final_answer

    pay_months = calculateMonthsUntilPaidOff(balance, payment, daily_apr)

    print("It will take you {} months to pay off this card.".format(pay_months))


#Problem 12. take several pieces of information from user and validate each piece separately

#def problemtwelve():
#    def inputs:
#    firstname = input("Enter the first name: ")
#    lastname = input("Enter the last name: ")
#    zipcode = input("Enter the zip code: ")



#    def Name_Test(x):
#        if len(x) >= 2:
#            d = 1
#        else:
#            d = 0
#        return d



#    def ZipCode_Test():
#       zipcode = input("Enter the zip code: ")
#        if str.isdigit(zipcode):
#            zipcode = 1
#        else:
#            zipcode = 0
#        return zipcode

#    def all_tests_combined(firstname, lastname, zipcode):
#        if Name_Test(firstname) == 0:
#            print('"{}" is not a valid first name. It is too short.')
#        if Name_Test(lastname) == 0:
#            print('"'{}" is not a valid last name. It is too short. ')
#        if ZipCode_Test(zipcode) == 0:
#            print('"{}" is not a valid zip code.')
#        if


#    firstname_value = FirstName_Test(firstname)
#    print(firstname_value, firstname)

#problemtwelve()

#
#Problem 13. Prompt user for 5 numbers and computes the total of the numbers
def problemthirteen():
    final_number = 0

    for i in range(5):
        numberi = int(input("Enter a number: "))
        final_number += numberi
    print("The total is {}.".format(final_number))

#Problem 14.Write a calculator that prompts for the rate of return on an investment and calculates how many years to
# double investment
def problemfourteen():

    while True:
        try:
            rate = float(input("What is the rate of return? "))
        except ValueError:
            print("Sorry. That's not a valid input. ")
            continue
        if rate == 0:
            print("Sorry. That's not a valid input. ")
            continue
        else:
            break
    years = round((72 / rate),2)
    print("It will take {} years to double your initial investment".format(years))


#Problem 15. create a program that generates multiplication tables for number 0 to 12

def problemfifteen():
    n = int(input("What multiplication table would you like to see?"))
    for row in range (1,n+1):
        s = ""
        for col in range(1,n+1):
            s += '{:3} '.format(row * col)
        print(s)


#Problem 16. Take in the users age and resting heartrate and determine the 55% - 95% (by 5%) heart rates.
def problemsixteen():
    while True:
        try:
            age = int(input("What is your age? "))
            heartrate = int(input("What is your reseting heartrate? "))
        except ValueError:
            print("Sorry. That is not a valid input. Please enter a number. ")
            continue
        else:
            break
    intensity = 0.95
    target_hr = (((220 - age) - heartrate) * intensity) + heartrate

    print("Intensity    |    Rate")
    print("_ _ _ _ _ _  | _ _ _ _")

    for percent in range(55, 100, 5):
        target_intensity = percent / 100
        target_hr = round((((220 - age) - heartrate) * target_intensity) + heartrate)
        print("{}%          |    {} bmp".format(percent, target_hr))


#Problem 17. Create a game with 3 difficulty levels and generate a random number. Count how many times it takes the
#to pick the correct number.
def problemseventeen():
    import random
    print("Let's play Guess the Number.")
    while True:
        try:
            game_type = int(input("Pick a difficulty level (1, 2, 3): ? "))
        except ValueError:
            print("Sorry. That is not a valid input. Please enter a number. ")
            continue
        else:
            break
    print(game_type)
    counter = 0
    if game_type == 1:
        game_number = random.randint(1,10)
    elif game_type == 2:
        game_number = random.randint(1,100)
    elif game_type == 3:
        game_number = random.randint(1,1000)
    else:
        return
    print(game_number)


    def Game(x, counter):
        guess = int(input("I have my number. What's your guess"))
        counter = counter + 1
        if guess < x:
            print("Too Low. Guess Again: ")
            Game(x, counter)
        elif guess > x:
            print("Too high. Guess Again: ")
            Game(x, counter)
        else:
            print("You got it in {} guesses!".format(counter))

    final_test = Game(game_number, counter)
    print(final_test)
    print(game_number)


#Problem 18. Create a Magic 8 ball game.

def problemeighteen():
    import random
    question = input("What's your question? ")
    random_number = random.randint(1, 4)
    options = ["Yes", "No", "Maybe", "Ask again later"]

    print(options[(random_number - 1)])
    replay = input("Would you like to play again (Y/N)? ")
    if replay.upper() == "Y":
        problemeighteen()
    else:
        return

#Problem 19. Print a list of names and ask which to delete. Then re-print the list with the name removed.

def problemnineteen():
    employee_list = ["John Smith", "Jackie Jackson", "Chris Jones", "Amanda Cullen", "Jeremy Goodwin"]

    for element in  employee_list:
        print(element)

    while len(employee_list) != 0:
        name_remove = input("What name do you want to remove: ")
#        print(employee_list.index(name_remove))
        delete_name = employee_list.index(name_remove)
        del employee_list[delete_name]
        for element in  employee_list:
            print(element)


#Problem 20. Create program that picks a winner from a

def problemtwenty():
    import random
    contest_list = []
    user_input = 0

    while user_input != "":
        user_input = input("Enter a name: ")
        contest_list.append(user_input)

    print(contest_list)


    winner = random.randint(1,len(contest_list))
    print(contest_list)
    print(winner)
    print("The winner is... {}.".format(contest_list[(winner - 1)]))


#Problem 21. Take in several inputs from user and find several arithmetic values from the inputs

def problemtwentyone():
    import numpy
    import math

    time_list = []
    user_input = 0

    while True:
        try:
            user_input = int(input("Enter a number: "))
            time_list.append(user_input)
        except ValueError:
            break

    average = sum(time_list)/len(time_list)
    minimum = min(time_list)
    maximum = max(time_list)
    standard_deviation = numpy.std(time_list)


    print("Numbers: {}".format(time_list))
    print("The average is {}".format(average))
    print("The minimum is {}".format(minimum))
    print("The maximum is {}".format(maximum))
    print("The standard deviation is {}".format(standard_deviation))


#Problem 22. http://stackoverflow.com/questions/2823316/generate-a-random-letter-in-python
def problemtwentytwo():
    import string
    import random
    min_length = int(input("What is the minimum length? "))
    number_of_special = int(input("How many special characters? "))
    number_of_numbers = int(input("How many numbers? "))
    true_minimum = max((number_of_numbers + number_of_special), min_length) + 5

    additional_chars = ''.join(random.choice(string.ascii_letters) for i in range(true_minimum - number_of_special -
                                                                                  number_of_numbers))
    special_char = ''.join(random.choice(string.punctuation) for i in range(2))
    numbers = ''.join(random.choice(string.digits) for i in range(number_of_numbers))
    password = additional_chars + special_char + numbers
    shuffle_password = ''.join(random.sample(password, len(password)))
    print("Your password is \n {}".format(shuffle_password))


problemtwentytwo()


#problemone()
#problemtwo()
#problemthree()
#problemfour()
#problemfive()
#problemsix()
#problemseven()
#problemeight()
#problemnine()
#problemten()
#problemeleven()
#problemthirteen()
#problemfourteen()
#problemfifteen()
#problemsixteen()
#problemseventeen()
#problemeighteen()
#problemnineteen()
#problemtwenty()
#problemtwentyone()