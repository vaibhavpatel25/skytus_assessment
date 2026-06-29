#username and password verification.

Data={
    "vanshpatel7":1234,
    "manrabari18":2222,
    "lears18":0000,
    "shivam1726":4545,
    "dhruvptl018":6666
}

Username=input("Enter the username :")
Password=int(input("Enter the password :"))

if Username in Data and Data[Username]==Password:
    print("Wellcome back")
else:
    print("Enter a valid username and password")
