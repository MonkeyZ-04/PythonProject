def run():
    checkthree = ["3", "4", "7"]
    checktwonum1 = ['21', '23', '25', '28']
    checktwonum2 = ['22', '24', '26', '27']

    ID = input("Enter student ID: ")

    if len(ID) == 10 and ID[2] in checkthree and int(ID[8:10]) in range(21, 29) and int(ID[0:2]) in range(50, 67):
        semester = input("Enter semester: ")
        if ID[8:10] in checktwonum1:
            if semester == "1" or semester == "2":
                if int(ID[0:2]) in range(50, 56) and (ID[2] == "3" or ID[2] == "4"):
                    print("Registration fee : 18000")
                elif int(ID[0:2]) in range(56, 67) and (ID[2] == "3" or ID[2] == "4"):
                    print("Registration fee : 21000")
                elif int(ID[0:2]) in range(50, 56) and ID[2] == "7":
                    print("Registration fee : 26000")
                elif int(ID[0:2]) in range(56, 67) and ID[2] == "7":
                    print("Registration fee : 31000")
            elif semester == "3":
                if int(ID[0:2]) in range(50, 56) and (ID[2] == "3" or ID[2] == "4"):
                    print("Registration fee : 4500")
                elif int(ID[0:2]) in range(56, 67) and (ID[2] == "3" or ID[2] == "4"):
                    print("Registration fee : 5250")
                elif int(ID[0:2]) in range(50, 56) and ID[2] == "7":
                    print("Registration fee : 7000")
                elif int(ID[0:2]) in range(56, 67) and ID[2] == "7":
                    print("Registration fee : 7750")
            else:
                print("Invalid semester")
        elif ID[8:10] in checktwonum2:
            if semester == "1" or semester == "2":
                if int(ID[0:2]) in range(50, 56) and (ID[2] == "3" or ID[2] == "4"):
                    print("Registration fee : 14500")
                elif int(ID[0:2]) in range(56, 67) and (ID[2] == "3" or ID[2] == "4"):
                    print("Registration fee : 17000")
                elif int(ID[0:2]) in range(50, 56) and ID[2] == "7":
                    print("Registration fee : 19000")
                elif int(ID[0:2]) in range(56, 67) and ID[2] == "7":
                    print("Registration fee : 23000")
            elif semester == "3":
                if int(ID[0:2]) in range(50, 56) and (ID[2] == "3" or ID[2] == "4"):
                    print("Registration fee : 4500")
                elif int(ID[0:2]) in range(56, 67) and (ID[2] == "3" or ID[2] == "4"):
                    print("Registration fee : 5250")
                elif int(ID[0:2]) in range(50, 56) and ID[2] == "7":
                    print("Registration fee : 7000")
                elif int(ID[0:2]) in range(56, 67) and ID[2] == "7":
                    print("Registration fee : 7750")
            else:
                print("Invalid semester")
        else:
            print("Invalid ID")
    else:
        print("Invalid ID")
run()