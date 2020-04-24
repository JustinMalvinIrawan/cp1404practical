def main():
    email_to_name = {}
    user_email = input("Please enter your email:")
    while user_email != "":
        name = split_name_from_email(user_email)
        confirmation = input("Is your name {}? (Y/n) ".format(name))
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        email_to_name[user_email] = name
        user_email = input("Email: ")

    for user_email, name in email_to_name.items():
        print("{} ({})".format(name, user_email))


def split_name_from_email(user_email):
    split_name = user_email.split("@")[0]
    parts = split_name.split(".")
    name = " ".join(parts).title()
    return name


if __name__ == "__main__":
    main()