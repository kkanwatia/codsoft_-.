import random
capital = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
small = [letter.lower() for letter in capital]
number = [str(i) for i in range(0,10)]
special = "!@#'$%^&*()_+-=[]{}|;:,.<>/?"

user=[]
def ask():
    length = int(input("Specify the length of the password: "))
    capital_input = input("Do you want capital letters in your password? y/n: ").lower()
    small_input = input("Do you want small letters in your password? y/n: ").lower()
    num_input = input("Do you want numbers in your password? y/n: ").lower()
    special_input = input("Do you want specail characters in your password? y/n: ").lower()
    return length ,capital_input,small_input,num_input,special_input

def password(user_input):
    list_choice = []
    if user_input[1] == "y":
        list_choice.append(capital)
    if user_input[2] == "y":
        list_choice.append(small)
    if user_input[3] == "y":
        list_choice.append(number)
    if user_input[4] == "y":
        list_choice.append(special)
    
    for _ in range(user_input[0]):
        type_chosen = random.choice(list_choice)
        pass_chosen = random.choice(type_chosen)
        user.append(pass_chosen)


ask_list  = ask()
password(ask_list)
dummy_str =''
print(dummy_str.join(user))

# password_string =''
# for i in range(len(user)):
#     password_string += user[i]
# print(password_string)