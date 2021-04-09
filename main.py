#Password Generator Project
from random import *
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
all_nr = nr_letters+nr_numbers+nr_symbols
password = []
for sym in range (0, nr_letters):
  password.insert(randint(0, all_nr) , letters[randint(0, len(letters)-1)])
for sym in range (0, nr_symbols):
  password.insert(randint(0, all_nr), symbols[randint(0, len(symbols)-1)])
for sym in range (0, nr_numbers):
  password.insert(randint(0, all_nr), numbers[randint(0, len(numbers)-1)])
user_password = ("")
for i in range (0, len (password)):
  user_password += password [i]
# print (password)
print (f"Your password:   {user_password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&