import random
import string


def generate_password(min_length, numbers=True, special_character=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_character:
        characters += special

    psd = ""
    meet_criteria = False
    has_number = False
    has_special = False
    while not meet_criteria or len(psd) < min_length:
        new_char = random.choice(characters)
        psd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meet_criteria = True
        if numbers:
            meet_criteria = has_number
        if special_character:
            meet_criteria = meet_criteria and has_special
    return psd



min_length = int(input("enter minimun length "))
has_number = input("do you want to have a number?(y/n)").lower() == "y"
has_special = input("do you want to have special characters?(y/n)").lower() == "y"

psd = generate_password(min_length, has_number, has_special)
print("the password generated is :", psd)




