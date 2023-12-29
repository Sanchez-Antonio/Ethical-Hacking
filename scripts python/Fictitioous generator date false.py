import os
from faker import Faker

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_personal_data():
    fake = Faker()
    print(f"NAME : {fake.name()}\nEmail : {fake.email()} \nPhone Number : {fake.phone_number()}\nAddress : {fake.address()}")

def generate_address():
    fake = Faker()
    print(f"Address : {fake.address()}")

def generate_companies():
    fake = Faker()
    print(f"Company Name : {fake.company()}")
    print(f"Industry : {fake.bs()}")

def generate_dates():
    fake = Faker()
    print(f"Date in this century : {fake.date_this_century()}")
    print(f"Time of day : {fake.time()}")

def generate_networks():
    fake = Faker()
    print(f"Fictitious URL : {fake.url()}")
    print(f"Fictitious IPv4 Address : {fake.ipv4()}")
    print(f"Fictitious User Agent : {fake.user_agent()}")

def generate_credit_card():
    fake = Faker()
    print(f"Fictitious Credit Card Number : {fake.credit_card_number()}")
    print(f"Fictitious Credit Card Expiry Date : {fake.credit_card_expire()}")
    print(f"Fictitious Credit Card Security Code : {fake.credit_card_security_code()}")

def main():
    while True:
        clear_screen()
        print("""\t \n Generate Fake Data\n  
        
        1. Personal Dates
        2. Address
        3. Companies
        4. Dates
        5. Networks
        6. Credit Card
        7. Close Program
        """)
            
        print("")

        selected = int(input("Enter an option -->"))

        if selected == 1:
            clear_screen()
            generate_personal_data()
        elif selected == 2:
            clear_screen()
            generate_address()
        elif selected == 3:
            clear_screen()
            generate_companies()
        elif selected == 4:
            clear_screen()
            generate_dates()
        elif selected == 5:
            clear_screen()
            generate_networks()
        elif selected == 6:
            clear_screen()
            generate_credit_card()
        elif selected == 7:
            print("CLOSE PROGRAM")
            break
        else:
            print("Invalid Option")

        input("Press Enter to continue...")

if __name__ == "__main__":
    main()
