# Create an account - Name, Surname, ID, email, password
# Login - ID/email and password

applicants = [
    {"name":"Sherith","surname":"Baloyi","id":"0412270522086","email":"sherith@gmail.com","password":"Sherith@27"},
    {"name":"Siamang","surname":"Khoza","id":"0112050522086","email":"siakhoza@gmail.com","password":"Siamang@05"}
]

print("""
******************************* WELCOME TO PYTHON ACADEMY*******************************

                               CREATE YOUR ACCOUNT""")

id_num = input("Please enter your ID number: ")

matched_applicant = next((a for a in applicants if a['id'] == id_num), None)

if matched_applicant:
    print("Your account already exists!!!")
else:
    first_name = input("Please enter your first name: ")
    surname = input("Please enter your surname: ")
    email_address = input("Please enter your email address: ")
    password_1 = input("Please enter a strong password: ")
    applicants.append(
        {"name":first_name,"surname":surname,"id":id_num,"email":email_address,"password":password_1}
    )
    print("Your account has been created successfully!!!")
    matched_applicant = applicants[-1]  # the newly created account

# Show account details
print(f"""
HERE ARE YOUR ACCOUNT DETAILS: 
    
NAME: {matched_applicant['name']}
SURNAME: {matched_applicant['surname']}
ID: {matched_applicant['id']}
EMAIL: {matched_applicant['email'][:3]}*******@gmail.com
PASSWORD: {matched_applicant['password'][0]}*********{matched_applicant['password'][-1]}
""")

print("""
                                       LOGIN                                                    """)

# Login attempts
for i in range(3):
    username = input("Please enter your email: ")

    matched_applicant = next((a for a in applicants if a['email'] == username), None)

    if matched_applicant:
        for j in range(3):
            user_password = input("Please enter your password: ")

            if user_password == matched_applicant['password']:
                print("You have successfully logged in!!!")
                exit()
            else:
                print("Incorrect password!!!")

        print("Login Failed! Reached maximum number of password attempts.")
        print("Contact admin: 0754967643")
        exit()
    else:
        print("Incorrect email!!!")

print("Login Failed! Reached maximum number of email attempts.")
print("Contact admin: 0754967643")

# ENHANCEMENTS
# - The programmer(Sheri) Can view all students who have an account(TO DO)
# User(Those who already have an account) can log in. # If not allow the user to create one (DONE)
# Can attempt to log in only 3 times if the first 2 attempts were incorrect(DONE)

#Suggested enhancements:
# Add a menu to choose between logging in and creating an account
