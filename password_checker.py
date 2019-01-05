correct_password = "python123"
name = input("Please enter your name: ")
surname = input("Please enter your surname: ")
password =input("Please enter password: ")

while correct_password != password:
    password = input("wrong password! Enter Again: ")

print("Hi %s %s, you are logged In"  % (name,surname))