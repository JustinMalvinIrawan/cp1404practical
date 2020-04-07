minimum_length = 4

def main():
    password = get_password()
    while len(password)<minimum_length:
        password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    print('*' * len(password))


def get_password():
    password = input("Please enter your password at least {} length".format(minimum_length))
    return password


main()