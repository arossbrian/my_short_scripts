userNames = []

if userNames:

    for name in userNames:
        if name == 'admin':
            print("Hello {}, would you like a status report ?".format(name))
        else:
            print("Hello {}, thank you for logging in again".format(name))
else:
    print("We need to find some users")
