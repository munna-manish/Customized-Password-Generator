#This the Password Generating code with high security

import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','&','-','{','}']

user_letters = int(input("How many letters do you want in your password? Enter here:"))
user_numbers = int(input("How many numbers do you want in your password? Enter here:"))
user_symbols = int(input("How many symbols do you want in your password? Enter here:"))

password = ""

for char in range(0,user_letters):
    password += random.choice(letters)

for num in range(0,user_numbers):
    password += random.choice(numbers)

for symbol in range(0,user_symbols):
    password += random.choice(symbols)

print("Your password can be: '",password,"'")