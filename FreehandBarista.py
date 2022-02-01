print("Hello, welcome to this bar.")

name = (input("What is your name? \n")) 

print ("Good to see you " + name)

age = (input("To be able to drink here you have to be of age, how old are you " + name + "? "))

if int(age) >= 18:(
    print("Thank you, what do you want to drink?")
)
else: 
    print("I am sorry, you are not of age")
    exit()

menu = ("Beer, Cider, Seltzer, Alcohol free beer")

order = input("Our menu is " + menu + "\n")

price = 90

amount = input("Great! How many " + order + " would you like? ")

total = price * int(amount)

print("Here is your" + order + ". The price will be " + str(total))