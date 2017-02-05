#Program 1. Take an input and print the input within a sentence

def programone():
    name = input("What is your name? ")
    greeting = "Hello, " + name + ", nice to meet you!"
    print(greeting)


#Program 2. Take an input and print the input as well as the length of the input.

def programtwo():
    name2 = input("What is the input string? ")
    print(name2, "has", len(name2), "characters")


#Program 3. create a mad libs game by taking several inputs from the user without explaining what the final ouput will be

def programthree():
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    adverb = input("Enter an adverb: ")
    print("Do you", verb, "your", adjective, noun, adverb,"? That's hilarious!")


#Program 4. Take 2 inputs and return the sum, difference, product and quotient of the two numbers
def programfour():
    numberone = input("What is the first number?")
    numbertwo = input("What is the second number?")
    convertnumberone = float(numberone)
    convertnumbertwo = float(numbertwo)
    addition = convertnumberone + convertnumbertwo
    subtraction = convertnumberone - convertnumbertwo
    product = convertnumberone * convertnumbertwo
    quotient = convertnumberone / convertnumbertwo
    print(numberone , "+ " , numbertwo , " = " , addition , "\n",
          convertnumberone , "-" , numbertwo , "=", subtraction, "\n",
          convertnumberone , "*" , numbertwo , "=", product, "\n",
          convertnumberone , "/", numbertwo , "=", quotient, "\n",)



#Program 5. Create a program that takes your current age, expected age of of retirement and provides back the year

def programfive():
    import datetime
    now = datetime.datetime.now()
    currentage = int(input("What is your current age?"))
    retireage = int(input("What age would you like to retire?"))
    retiretime = retireage - currentage
    currentyear = now.year
    retireyear = currentyear + retiretime
    print("You have " , retiretime , "years left until you retire")
    print("It is ", currentyear , "so you can retire in", retireyear)


#Program 6. take the length and width of a room and return the square feet and square meters of the room
def programsix():

    length = int(input("What is the length of the room?"))
    width = int(input("What is the widgth of the room?"))
    feetroom = length * width
    meterstofeet = feetroom * 0.09290304

    print("The area is " , "\n",
          feetroom , "square feet" , "\n" ,
          meterstofeet , "square meters")


#Program 7. Take the number of pizzas, number of slices per pizza and number of people and calculate how many slices
#each person gets

def programseven():

    people = int(input("How many people are there?"))
    pizza = int(input("How many pizzas are there?"))
    slices = int(input("How many slices per pizza?"))
    total_slices = pizza * slices
    extra_slices = people % total_slices
    slices_per_person , remaining= divmod(total_slices, people)

    print("{} people with {} pizzas".format(people, pizza))
    print("Each person gets {} slices of pizza".format(slices_per_person))
    print("There are {} leftover pieces.".format(remaining))



#Program 8. Calculate the paint needed to pain the ceiling of the room. Bring in the length and width in feet
# and divide the sq ft of the room by 350

def programeight():
      import math

      length = float(input("What is the length of the room in feet?"))
      width = float(input("What is the widgth of the room in feet?"))
      total_size = length * width
      convert = 350
      gallons = math.ceil(total_size / convert)
      output = "You will need to purchase {} gallons of paint to cover {} square feet".format(gallons, total_size)

      print(output)


#Program 9. create a simple check out system using several variables provided by user

def programnine():

      price1 = float(input("Enter the price of the item 1: "))
      quantity1 = float(input("Enter the quantity of the item 1: "))
      price2 = float(input("Enter the price of the item 2: "))
      quantity2 = float(input("Enter the quantity of the item 2: "))
      price3 = float(input("Enter the price of the item 3: "))
      quantity3 = float(input("Enter the quantity of the item 3: "))
      subtotal = price1*quantity1 + price2*quantity2 + price3*quantity3
      tax_rate = subtotal * 0.055
      total_bill = subtotal + tax_rate
      subtotal_string = "Subtotal: ${0:.2f}".format(subtotal)
      tax_string = "Tax: ${0:.2f}".format(tax_rate)
      total_string = "Total: ${0:.2f}".format(total_bill)



      print(subtotal_string)
      print(tax_string)
      print(total_string)


#Problem 10. Create a simple interest calculator

def problemten():
      import decimal

      principal = float(input("Enter the principal: "))
      interest = float(input("Enter the rate of interest: "))
      years = float(input("Enter the number of years: "))
      interest_calc = interest / 100
      total_investment = principal*(1 + interest_calc*years)
      total_investment_round = round(total_investment + 0.005, 2)

      print(total_investment_round)




programone()
programtwo()
programthree()
programfour()
programfive()
programsix()
programseven()
programeight()
programnine()
problemten()
