from spy_details import Spy_Name, Spy_Rating, Spy_Age

print "Hello!!! \nWelcome To SpyChat."

STATUS_MESSAGE = ["Hey..!!", "All_Good", "Namaskar" "All Is Well"]

friends_name = []
friends_age = []
friends_Code_Name = []
friend_is_online = []


def add_status(c_status):
    if c_status != None:
        print "your current status is " + c_status
    else:
        print "you don't have any status currently"
    existing_status = raw_input("Do you want to add new status? Y/N ")
    if existing_status.upper() == "Y":
        new_status = raw_input("Enter your status: ")
        if len(new_status) > 0:
            STATUS_MESSAGE.append(new_status)

    elif existing_status.upper() == "N":
        serial_no = 1
        for old_status in STATUS_MESSAGE:
            print str(serial_no) + ". " + old_status
            serial_no = serial_no + 1
        user_choice = input("Enter your choice: ")
        new_status = STATUS_MESSAGE[user_choice - 1]
    update_status = new_status
    return update_status


def add_friend():
    frnd_name = raw_input("What is your name? ")
    frnd_age = input("What is your age? ")
    frnd_code_name = raw_input("What is your code name? ")
    if len(frnd_name) > 3 and 18 < frnd_age < 50 and frnd_code_name > 3:
        friends_name.append(frnd_name)
        friends_age.append(frnd_age)
        friends_Code_Name.append(frnd_code_name)
        friend_is_online.append(True)
    else:
        print "Friend's Can't be added"
    return len(friends_name)


def Start_Chat(Spy_Code_Name, Spy_Age):
    print Spy_Code_Name + " What Do You Want To Do?"

    current_status = None

    Show_Menu = True
    while Show_Menu:
        Choices = input("1. Update Status \n2. Add A Friend \n3. Send A Message \n0. Exit ")
        if Choices == 1:

            current_status = add_status(current_status)
            print "updated status " + current_status
#use nested if
        elif Choices == 2:

            no_of_friends = add_friend()
            print "you have " + str(no_of_friends) + " friends"
            print "your friend list is: \n" \
                  "" +str(friends_name)

        elif Choices == 3:
            Message = raw_input("Type A Message To Send. ")
            print "Your Message \n" + Message
        elif Choices == 0:
            Show_Menu = False
            print "Hope You Enjoyed The Session. \nHave A Good Day..!!"
        else:
            print "Choose A Correct Option."


Existing_Spy = raw_input("Are You A New User (Y/N) ")

if Existing_Spy == "N".lower() or Existing_Spy == "n".upper():
    print "Welcome Back Agent " + Spy_Name + ". \nSpy Rating " + str(Spy_Rating) + "\nAge " + str(Spy_Age)
    Start_Chat(Spy_Rating, Spy_Age)


elif Existing_Spy == "Y".lower() or Existing_Spy == "y".upper():
    Spy_Name = raw_input("What's Your Name? ")
    if len(Spy_Name) > 3:
        print "Welcome " + Spy_Name + " Glad to see you."

        Spy_Salutation = raw_input("What should we call you (Mr. or Ms.)? ")
        # #use .upper for change alphabet foramt in upper case.

        if Spy_Salutation == "Mr".upper() or Spy_Salutation == "Ms".upper() or \
                        Spy_Salutation == "Mr".lower() or Spy_Salutation == "Ms".lower() or \
                        Spy_Salutation == "Mr".isspace():


            Spy_Name = Spy_Salutation + " " + Spy_Name

            print "Alright " + Spy_Name + " " + "We Would Like To Know A Little Bit More About You..."
            spy_age = 0

            spy_raiting = 0.0  # use for known about spy_qualification.

            spy_is_online = True

            spy_age = input('what is your age?')

            if 50 > spy_age > 12:

                print "your age is correct"

                spy_raiting = input('what is your raiting?')

                if spy_raiting > 5.0:  # nested if

                    print "great spy"

                elif 3.5 < spy_raiting <= 5.0:

                    print "avg. spy"

                elif 2.5 < spy_raiting <= 3.5:

                    print "bad spy"

                else:

                    print " who hired you? "

                spy_is_online = True

                print "Authentication Complete Welcome " + Spy_Name + " age:" + str(spy_age) + " raiting:" + str(

                    spy_raiting)

            else:

                print "you are not eligible for spy..!!"

        else:

            print "invalid salution"

    else:

        print "ooopss please enter valid name"

else:

    print"invalid entry"










