#password generator
import random
import string
import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="sakshi@123",
    database="PASSWORDS"
)
cursor=db.cursor()


def generate_password(length):
    characters = (
        string.ascii_letters +
        string.digits 
    )

    passwords = ''.join(random.choice(characters) for _ in range(length))
    return passwords

def main():
    print("=== Password Generator ===")

    while True:
        site=input("for which site u want to create password : ")
        site=site.upper()

        try:
            length = int(input("Enter password length: "))

            if length < 4:
                print("Password length should be at least 4.")
                continue

            passwords = generate_password(length)
            print("\nGenerated Password:")
            print(passwords)
            sql="INSERT INTO PASS (site,passwords) VALUES(%s,%s)"
            values=(site,passwords)
            cursor.execute(sql,values)
            db.commit()
            print("password saved successfully ✅")

            again = input("\nGenerate another? (y/n): ").lower()
            if again != 'y':
                print("Goodbye!")
                break

        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()