minimum_length = 4

def main():
    password = input("Please enter your password at least {} length".format(minimum_length))
    while len(password)<minimum_length:
        password = input("Please enter your password at least {} length".format(minimum_length))
    print('*' * len(password))



main()