from encryptLib import save, searchNCheck

def getUser():
    uname, pwd = input("Username : "), input("Password : ")
    save(uname, pwd)

def login():
    uname, pwd = input("Username : "), input("Password : ")
    if searchNCheck(uname, pwd):
        print("Logged in!")
    else:
        print("Failed, check your pwd!")

def main():
    while True:
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        ans = input("choose : ")
        if ans == "1":
            login()
        elif ans == "2":
            getUser()
        elif ans == "3":
            break
        else:
            print("Wrong option")

if __name__ == "__main__":
    main()