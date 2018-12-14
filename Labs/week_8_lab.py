import random

'''d = 50506.2124524342352525242
print("The value of d is: {0:10.2f}".format(d))

user_input = int(input("Please input an integer value: ")) # Takes a user input


print ("The binary value is: {0:b}".format(user_input)) #Converts the user input to hex and binary
print ("The hex point value is: {0:x}".format(user_input))

a = "animal"
b = "horse"
print("My favourite {:10s} is {}".format(a,b))'''


def writeCurrency(currency, amount):
    type = ['$', '£', '€', '₪']
    currency = random.choice(type)
    amount = random.randint(1,1000)

    print("{}{.f}".format(currency,amount))


writeCurrency()
