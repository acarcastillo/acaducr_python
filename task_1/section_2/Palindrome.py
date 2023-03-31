def is_palindrome(input_user):
    input_user = input_user.replace(" ", "").lower()
    return input_user == input_user[::-1]


def validate_input_user(): 
    input_user = str(input("Ingrese un palindromo \n"))

    if is_palindrome(input_user):
        print(f" The phrase '{input_user}' is a palindrome")
    else:
        print("The phrase '{}' is not a palindrome".format(input_user))

if __name__ == '__main__':
    validate_input_user()        




