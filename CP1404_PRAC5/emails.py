def main():
    email_name = {}
    email = input("Email: ")
    while email != "":
        name = name_of_email(email)
        answer = input("Is your name {}? (Y/n) ".format(name))
        if answer.upper() != "Y" and answer != "":
            name = input("Name: ")
        email_name[email] = name
        email = input("Email: ")

    for email, name in email_name.items():
        print("{} ({})".format(name, email))

def name_of_email(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name

main()