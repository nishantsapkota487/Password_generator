# password generator project

import random

class Password:
    def __init__(self):
        #Characters to use in the password
        self.uppercase = [ chr(i) for i in range(65, 90) ]
        self.lowercase = [ chr(i) for i in range(97, 122) ]
        self.numbers = [ i for i in range(1, 10) ]
        self.special_char = [ chr(i) for i in range(33, 47) ]
        self.num_password = int(input("Enter the number of password you want: "))

    #This method generates the uppercase letters for the password
    def generate_uppercase(self):
        num_uppercase = int(input("Enter the number for uppercase; "))
        while num_uppercase < 1 or num_uppercase > 5:
            num_uppercase = int(input("uppercase should not be less than 1 or more than 5. "))
        upper_case_letters = ''
        for i in range(num_uppercase):
            upper_case_letters += random.choice(self.uppercase)
        return list(upper_case_letters)


    #This method generates the lowercase letters for the password
    def generate_lowercase(self):
        num_lowercase = int(input("Enter the number for lowercase"))
        while num_lowercase < 1 or num_lowercase > 5:
            num_lowercase = int(input('uppercase should not be less than 1 or more than 5. '))
        lower_case_letters = ''
        for i in range(num_lowercase):
            lower_case_letters += random.choice(self.lowercase)
        return list(lower_case_letters)

    #This method generates the numbers for the password
    def generate_numbers(self):
        num_numbers = int(input("Enter the number for numbers"))
        while num_numbers < 1 or num_numbers > 5:
            num_numbers = int(input("numbers cannot be less than 1 or cannot be greater than 5: "))
        numbers = ''
        for i in range(num_numbers):
            numbers += str(random.choice(self.numbers))
        return list(numbers)


    #This method generates the special characters for the password
    def generate_special_chars(self):
        num_special_chars = int(input('Enter the number of special chars: '))
        while num_special_chars < 1 or num_special_chars > 5:
            num_special_chars = int(input("special chars cannot be more than 5 or less than 1"))
        special_chars = ''
        for i in range(num_special_chars):
            special_chars += random.choice(self.special_char)
        return list(special_chars)

    def generate_password(self):
        count = 1
        #list of final passwords
        final_passwords = []

        while True:
            print(f"Enter your requirements for password number { count }")
            password = ''
            uppercase_letters = self.generate_uppercase()
            lowercase_letters = self.generate_lowercase()
            special_chars = self.generate_special_chars()
            numbers = self.generate_numbers()

            #To ensure all the conditions set by the user are met
            while len(uppercase_letters) != 0 or len(lowercase_letters) != 0 or len(special_chars) != 0 or len(numbers) != 0:

                #This is to randomize the placing of uppercase, lowercase, special chars and numbers in the generated password
                choose_num = random.choice([1,2,3,4])

                if choose_num == 1 and len(uppercase_letters) > 0:
                    chosen_letter = random.choice(uppercase_letters)
                    password += chosen_letter
                    uppercase_letters.remove(chosen_letter)

                elif choose_num == 2 and len(lowercase_letters) > 0:
                    chosen_letter = random.choice(lowercase_letters)
                    password += chosen_letter
                    lowercase_letters.remove(chosen_letter)

                elif choose_num == 3 and len(special_chars) > 0:
                    chosen_letter = random.choice(special_chars)
                    password += chosen_letter
                    special_chars.remove(chosen_letter)

                elif choose_num == 4 and len(numbers) > 0:
                    chosen_letter = random.choice(numbers)
                    password += chosen_letter
                    numbers.remove(chosen_letter)

            final_passwords.append(password)
            count += 1
            print()

            #This is to print the generated passwords
            if count - 1 == self.num_password:
                print('Your passwords are: ')
                for i in final_passwords:
                    print(i)
                break



#main function of the code
def main():
    passwords = Password()
    passwords.generate_password()



main()
