#problem 1. Prompt user to enter order amount and state. If state is WI add 5.5% state tax. Return total
def problemone():
    import math
    orderamount = int(input("What is the order amount?"))
    state = input("What is the state?")
    tax = 0


    if state == 'WI' or state == 'wi' or state =='Wi' or state == 'wI':
        #The math.ceil will go to the next number up. This causes an issue if the number is 10 so i put it just below
        #0.05 to make sure it didn't round up in that instance. This will fail if someone uses more than 100,000,000
        tax = math.ceil(orderamount * 0.05499999 * 100) / 100
        print("The subtotal is: ${0:.2f}".format(orderamount))
        print("The tax is: ${0:.2f}".format(tax))

    total = round(orderamount + tax , 2)
    print("The total is ${}".format(total))


#Problem 2. Program to validate user input against a known system password value.

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


#Problem 4. Calculate the users Blood Alochol Content by taking several inputs from user.

def problemfour():
    try:
        gender = int(input("What is your gender? Enter 1 for Male, 0 for Female"))
        weight = int(input("What is your weight?"))
        drinks = int(input("How many drinks have you had?"))
        volume = int(input("What is the alcohol by volume per drink (in oz)?"))
        time = int(input("When was your last drink(in hours)"))
    except ValueError as e:
        print("You have entered an incorrect value. ")

    total_alcohol = drinks * volume
    #The below changes the ratio depending on if the user is a male or female.
    if gender == 1:
        ratio = 0.73
    else:
        ratio = 0.66

    bac = round((total_alcohol * 5.14 / weight * ratio) - 0.015 * time, 3)
    #The below is used to create only 1 output statement.
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

    #The below takes the user input, calculates the conversion and then passes 2 variables tot he single print
    #statement at the end.
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
    while True:
        try:
            weight = int(input("How much do you weigh?"))
            height = int(input("How tall are you in inches?"))
            break
        except ValueError as e:
            print("You have entered an incorrect value. ")
            continue

    bmi = (weight/(height **2)) * 703
    if 18.5 <= bmi <= 25:
        print("Your BMI is {:1f}".format(bmi))
        print("You are within the ideal weight range.")
    elif bmi < 18.5:
        print("Your BMI is {:1f}".format(bmi))
        print("You are underweight. You should see a doctor")
    else:
        print("Your BMI is {:1f}".format(bmi))
        print("You are overweight. You should see your doctr")



#Problem 7.Calculate tax, including state/county
def problemseven():
    order_amt = int(input("What is the order amount? "))
    state = input("What state do you live in (use abbreviation)? ")
    county = input("What county do you live in? ")
    state = state.upper()
    county = county.upper()
    tax = 0

    #This section validates the user input against several cases of county specific taxes. the values passed are all
    #upper case that were converted above so that way if a user types "Eau claire" it will still calculate correctly
    if state == 'WI' and county == 'EAU CLAIRE':
        tax = order_amt * (0.05 + 0.005)
    elif state == 'WI' and county == 'DUNN':
        tax = order_amt * (0.05 + 0.004)
    elif state == 'IL':
        tax = order_amt * 0.08
    else:
        tax = 0
    total = order_amt + tax

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
    password_test = ''
    password = ""

    def hasNumbers(x):
        return any(char.isdigit() for char in x)

    def specialchar(x):
        valid = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')
        return set(x).issubset(valid)


    #This function takes a supplied user password and validates it against several criteria. One criteria which is not
    #listed in the constraints is if the password is if it includes a special character but doesn't have numbers.
    #in this case I am re-calling the function to require the user to try again.
    def passwordValidator(password):
        password = input("What is your password: ")
        if str.isdigit(password) and len(password) < 8:
            return 'very weak'
        elif str.isalpha(password) and len(password) < 8:
            return 'weak'
        elif hasNumbers(password) and specialchar(password) and len(password) >= 8:
            return 'strong'
        elif hasNumbers(password) and specialchar(password) and str.isalpha(password) and len(password) >= 8:
            return 'very strong'
        else:
            print("Your password is not strong enough")
            passwordValidator(password)

    password_test = passwordValidator(password)

    print("The password {} is a {} password.".format(password, password_test))


#problem 11. Write a program to determine the length of time it will take to pay off a credit card.
def problemeleven():
    import math
    while True:
        try:
            balance = float(input("What is your balance? "))
            apr = float(input("What is the APR on the card (in percentage)?"))
            payment = float(input("What is the monthly payment you can make? "))
            daily_apr = apr / 365 / 100
            def calculateMonthsUntilPaidOff(balance,payment,daily_apr):
                log_test2 = 1 + balance / payment * (1 - (1 + daily_apr) ** 30)
                log_division = math.log(log_test2) / math.log((1 + daily_apr))
                final_answer = math.ceil(round((-1/30) * log_division) + 0.00001)
                return final_answer
            pay_months = calculateMonthsUntilPaidOff(balance, payment, daily_apr)
            break
            #If the combination of amount due, apr and payment are not enough to eventually pay off the balance
            #the above function will fail (the value passed to the log will be negative). This will prompt the user
            #to change some of the parameters.
        except ValueError:
            print("Either your APR is too high or your payment is too low. You will never pay this off. Please try "
                  "again.")
            continue

    print("It will take you {} months to pay off this card.".format(pay_months))


#Problem 12. take several pieces of information from user and validate each piece separately

def problemtwelve():

    def Name_Test(x):
        if len(x) >= 2:
            name = 1
        else:
            name = 0
        return name

    def ZipCode_Test(zipcode):
       if str.isdigit(zipcode):
           zip = 1
       else:
           zip = 0
       return zip


    #The below function uses 3 if statements due to the nature of the requirements for an employee ID. The first 2
    #characters must be letters. The 3 character must be a dash and the remaining characters must be numbers. If
    #any one of these fails, the function passes 0 and will fail in the below validateInput function
    def employee_ID_test(employee_ID):
        if employee_ID[0].isalpha():
            if employee_ID[1].isalpha():
                if employee_ID[2] == '-':
                    if employee_ID[3:].isdigit():
                        employee = 1
                    else:
                        employee = 0
                else:
                    employee = 0
            else: employee = 0
        else:
            employee = 0
        return employee


    #This function calls all of the above functions individually. If any of them fail, it provides the failure message
    #for the individual error. If any of them fail the function is re-called to re-input everything and retest.
    def validateInput():
        firstname = input("Enter the first name: ")
        lastname = input("Enter the last name: ")
        zipcode = input("Enter the zip code: ")
        employee_ID = input("Enter the employee ID: ")
        errors = 0
        if Name_Test(firstname) == 0:
            print('"{}" is not a valid first name. It is too short.'.format(firstname))
            errors = 1
        if Name_Test(lastname) == 0:
            print('"{}" is not a valid last name. It is too short.'.format(lastname))
            errors = 1
        if ZipCode_Test(zipcode) == 0:
            print('"{}" is not a valid zip code.'.format(zipcode))
            errors = 1
        if employee_ID_test(employee_ID) == 0:
            print('"{}" is not a valid employee ID code.'.format(employee_ID))
            errors = 1
        if errors == 1:
            validateInput()
        else:
            print("There were no errors found. ")

    test1 = validateInput()


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

    #This function has 2 failure options. the first is if the user enters a non-number. The second is if the user enters
    #a 0 for the rate of return. If either happen, it will start over.
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
    #This requires the user to input an integer. If not it will cycle back through.
    while True:
        try:
            age = int(input("What is your age? "))
            heartrate = int(input("What is your resting heartrate? "))
        except ValueError:
            print("Sorry. That is not a valid input. Please enter a number. ")
            continue
        else:
            break
    intensity = 0.95
    target_hr = (((220 - age) - heartrate) * intensity) + heartrate

    print("Intensity   |    Rate")
    print("_ _ _ _ _ _ | _ _ _ _")

    for percent in range(55, 100, 5):
        target_intensity = percent / 100
        target_hr = round((((220 - age) - heartrate) * target_intensity) + heartrate)
        print("{}%         |    {} bmp".format(percent, target_hr))


#Problem 17. Create a game with 3 difficulty levels and generate a random number. Count how many times it takes the
#to pick the correct number.
def problemseventeen():
    import random
    print("Let's play Guess the Number.")
    #This section is where the user selects the difficulty level. If they do not enter a number, it will fail and
    #require the user to re-enter a number.
    while True:
        try:
            game_type = int(input("Pick a difficulty level (1, 2, 3): ? "))
        except ValueError:
            print("Sorry. That is not a valid input. Please enter a number. ")
            continue
        else:
            break
    counter = 0
    #This section is where the random integer is selected. The variable game_number is passed a random number based on
    #the difficulty level of the game.
    if game_type == 1:
        game_number = random.randint(1,10)
    elif game_type == 2:
        game_number = random.randint(1,100)
    elif game_type == 3:
        game_number = random.randint(1,1000)
    else:
        return


    #This section is where the user makes their guesses. If the user inputs a non-integer, it will fail and reprocess.
    #A failure or an incorrect guess are counted as incorrect. Once the user selects the correct answer, the counter
    #is passed to the else: statement where it will tell the user how many guesses it took to correctly guess the number.
    def Game(x, counter):
        while True:
            try:
                guess = int(input("I have my number. What's your guess"))
                counter = counter + 1
                if guess < x:
                    print("Too Low. Guess Again: ")
                    continue
                elif guess > x:
                    print("Too high. Guess Again: ")
                    continue
                else:
                    print("You got it in {} guesses!".format(counter))
                    break
            except ValueError:
                print("Invalid entry, please guess a number.")
                counter = counter + 1
                continue

    final_test = Game(game_number, counter)


#Problem 18. Create a Magic 8 ball game.

def problemeighteen():
    import random
    question = input("What's your question? ")
    #This section creates a list out of the 4 possible answers and selects a random number between 1 and 4.
    random_number = random.randint(1, 4)
    options = ["Yes", "No", "Maybe", "Ask again later"]

    print(options[(random_number - 1)])
    #This section asks the user if they want to play again. If not, the function ends, if so the function calls itself
    #and the top part is looped again.
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
        delete_name = employee_list.index(name_remove)
        del employee_list[delete_name]
        for element in  employee_list:
            print(element)


#Problem 20. Create program that picks a winner from a

def problemtwenty():
    import random
    contest_list = []
    user_input = 0

    #This section creates the list of contestents that are entered by the user. Each time the user puts in a name, it is
    #added to the list contest_list. Once the user hits enter without typing anything, it moves on.
    while user_input != "":
        user_input = input("Enter a name: ")
        contest_list.append(user_input)


    #This selects a random number between 1 and the length of the list. That is passed to the final print statement.
    winner = random.randint(1,len(contest_list))
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


    print("Numbers: ", end= " ")
    for i in time_list:
        print("{}, ".format(i), end= " ")

    print("\nThe average is {:.2f}".format(average))
    print("The minimum is {}".format(minimum))
    print("The maximum is {}".format(maximum))
    print("The standard deviation is {:.2f}".format(standard_deviation))


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


#Problem 23. Take in a string of numbers separated by spaces and print out only the even numbers
def problemtwentythree():
    user_string = input("Enter a list of numbers separated by spaces. ")
    split_list = user_string.split(" ")
    split_list = [int(i) for i in split_list]
    split_list.sort()
    even_numbers = []

    def filterEvenNumbers():
        for i in split_list:
            if i % 2 == 0:
                even_numbers.append(i)
    test = filterEvenNumbers()
    print("The even numbers are", end=' ')
    size_even_numbers = len(even_numbers)
    for i in even_numbers:
        print(i, end=" ")


#Problem 24. Open a text file a map the columns into a table
def problemtwentyfour():
    data = [{"First Name":"John", "Last Name": "Johnson", "Position": "Manager", "Separation Date": "2016-12-31"},\
    {"First Name": "Tou", "Last Name": "Xiong", "Position": "Software Engineer", "Separation Date": "2016-10-15"},\
    {"First Name": "Michaela", "Last Name":"Michaelson", "Position":"District Manger","Separation Date": "2015-12-19"},\
    {"First Name": "Jake", "Last Name": "Jacobson", "Position": "Programmer", "Separation Date": ""},\
    {"First Name": "Jacquelyn", "Last Name": "Jackson", "Position": "DBA", "Separation Date": ""},\
    {"First Name": "Sally", "Last Name": "Weber", "Position": "Web Developer", "Separation Date": "2015-12-18"}]
    new_data = sorted(data, key=lambda k: k['Last Name'])

    #This is used to calculate the space that is needed for the print statement to look correct. It takes the longest
    #part of each section of the list and calculates the length. it is used in the bottom print statement.
    column1 = len(max(data[0]['First Name'], data[1]['First Name'], data[2]['First Name'], data[3]['First Name'],
                  data[4]['First Name'], data[5]['First Name'], key=len)) + 2
    column2 = len(max(data[0]['Last Name'], data[1]['Last Name'], data[2]['Last Name'], data[3]['Last Name'],
                  data[4]['Last Name'], data[5]['Last Name'], key=len)) + 2
    column3 = len(max(data[0]['Position'], data[1]['Position'], data[2]['Position'], data[3]['Position'],
                  data[4]['Position'], data[5]['Position'],key=len)) + 2

    print("Name                 | Position         | Separation Date".format())
    print("_ _ _ _ _ _ _ _ _ _ _| _ _ _ _ _ _ _ _ _| _ _ _ _ _ _ _ _")

    #This prints out the names and automatically extends the columns out to enough space to see each. If the data
    #got updated with a new longer name then this would re-adjust.
    for i in range(0,6):
        print("{:<{}}{:<{}}{:}".format(new_data[i]['First Name'] + " " + new_data[i]["Last Name"],
                                            column1 + column2, new_data[i]['Position'], column3,
                                            new_data[i]['Separation Date']))



#Problem 25. Similar to 24. Once 24 is done, work on 25
#def problemtwentyfive():



#Problem 26. Bring in CSV file and output names as well as the number of records
def problemtwentysix():
    import csv
    filename = 'Problem_26.csv'
    row_count = 0
    new_list = []

    with open(filename, 'r') as f:
        reader = csv.reader(f)
        your_list = list(reader)
        your_list.sort()
    for i in your_list:
        row_count = row_count + 1
    your_list_length = len(your_list)


    for i in range(your_list_length):
        new_list.append(your_list[i][0] + ", " + your_list[i][1])

    with open("Problem_26_output.csv", "w+") as f:
        writer = csv.writer(f)
        writer.writerow("Total of {} names".format(row_count))
        writer.writerow("_ _ _ _ _ _ _ _ _ _")
        writer.writerows(your_list)


    print("Total of {} names".format(row_count))
    print("_ _ _ _ _ _ _ _ _ _")
    for i in your_list:
        print("{}, {}".format(i[0],i[1]))


#Problem 27. Bring in a file and split the records without using import csv.
def problemtwentyseven():
    filename = 'Problem_27.csv'
    with open(filename, 'r') as f:
        results = []
        for line in f:
            words = line.split(',')
            results.append((words[0], words[1], words[2]))
#        print(type(results))
#        print(results)
    column1 = max(results[0][0], results[1][0], results[2][0], results[3][0], results[4][0], results[5][0],
                  results[6][0], key=len)
    column2 = max(results[0][1], results[1][1], results[2][1], results[3][1], results[4][1], results[5][1],
                  results[6][1], key=len)
    column1length = len(column1)+ 1
    column2length = len(column2) + 1

    print("{:<{}}{:<{}}Salary".format('Last', column1length, 'First', column2length))
    for i in range(0,7):
        print("{:<{}}{:<{}}${:,.2f}".format(results[i][0], column1length, results[i][1], column2length,
                                            int(results[i][2])))


#Problem 28. Import Json file, take input from user and retrieve the current price/quantity for that product.
def problemtwentyeight():
    import json
    with open('Problem_28.json') as json_data:
        data_file = json.load(json_data)
#        print(data_file)
#        print(type(data_file))
        validator = 0

        while validator == 0:
            user_input = input("What is the product name? ")
            for i in data_file['products']:
                if i['name'] == user_input:
                    print("Name: {}".format(i['name']))
                    print("Price: ${:.2f}".format(int(i['price'])))
                    print("Quantity on hand: {}".format(i['quantity']))
                    break
            else:
                print("Sorry, that product was not found in our inventory")



#Problem 29. Read a .txt file and replace all occurances of the word "Utilize" with "Use"
def problemtwentynine():
    file = open('Problem_29.txt')
    contents = file.read()
    print(contents)
    replaced_contents = contents.replace('utilize', 'use')
#    print(replaced_contents)
    new_file_name = input("What do you want the new file to be titled?")
    new_file = open('{}.txt'.format(new_file_name),'w+')
    new_file.write(replaced_contents)
    new_file.close()



#Problem 30, attempt 2 http://programminghistorian.org/lessons/counting-frequencies
def problemthirty():
    from collections import Counter
    filename = 'Problem_30.txt'
    with open(filename, 'r') as f:
        results = []
        for line in f:
            words = line.split(' ')
            results.append(words)

    word_count = Counter(results[0])
    print(word_count)
    print(type(word_count))

    bader_count = results[0].count('badger')
    mushroom_count = results[0].count('mushroom')
    snake_count = results[0].count('snake')
    print(bader_count, mushroom_count, snake_count)
    print(len(word_count))

    for key, value in word_count.most_common():
        number_stars = "*" * value
        print("{}: {}".format(key, number_stars))





#Need to confirm


problemtwentysix()





#Finalized
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
#problemtwelve()
#problemthirteen()
#problemfourteen()
#problemfifteen()
#problemsixteen()
#problemseventeen()
#problemeighteen()
#problemnineteen()
#problemtwenty()
#problemtwentyone()
#problemtwentytwo()
#problemtwentythree()
#problemtwentyfour()


#problemtwentyseven()
#problemtwentyeight()
#problemtwentynine()
#problemthirty()