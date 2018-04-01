from spy_details import Spy

#use module

from steganography.steganography import Steganography
from datetime import datetime
f = datetime.now()

print f
print "Hello!!! \nWelcome To SpyChat."

STATUS_MESSAGE = ["Hey..!!", "All_Good", "Namaskar" "All Is Well"]

friends = [{'Name':'Guru','Age':'22','Rating':'3.1','is_online':True,'chats':[]},{'Name':'HKC','Age':'21','Rating':'3.6','is_online':True,'chats':[]}]


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
    frnd ={
        'Name': 'HK',
        'Age': 0,
        'Rating': 0.0,
        'is_online':True,
        'chats': []
    }
    frnd['Name'] = raw_input("What is your name? ")
    frnd['Age'] = input("What is your age? ")
    frnd['Rating'] = raw_input("What is your Rating? ")
    if len(frnd['Name']) > 3 and 18 < frnd['Age'] < 50 and frnd['Rating'] > 3:
        friends.append(frnd)

    else:
        print "Friend's Can't be added"
    return len(friends)

def select_frnd():
    serial_no = 1
    for frnd in friends:
        print str(serial_no) + " " +frnd['Name']
        serial_no = serial_no+1
        user_selected_frnd = input("enter your choice : ")
        user_selected_frnd_index = user_selected_frnd - 1
        return user_selected_frnd_index
#use decode() incode() function

def Send_Message():
    selected_frnd = select_frnd()
    original_image = raw_input("what is the name of original image? ")
    secret_text = raw_input("what is your secret text? ")
    output_path = "output.jpg"
    Steganography.encode(original_image,output_path,secret_text)

    new_chat = {
        "message": secret_text,
        "time": datetime.now(),
        "sent_by_me": True
    }
    friends[selected_frnd]['chats']. append(new_chat)
    print "your secret message has been saved"

def read_message():
        selected_frnd = select_frnd()
        output_path = raw_input("which image you want to decode? ")
        secret_text = Steganography.decode(output_path)
        print "secret text is " + secret_text
        new_chat = {
            "message": secret_text,
            "time": datetime.now(),
            "sent_by_me": False
        }
        friends[selected_frnd]['chats'].append(new_chat)
        print "your secret message has been saved"


def Start_Chat(Spy_Name, Spy_Age):
    print Spy['Name'] + " What Do You Want To Do?"

    current_status = None

    Show_Menu = True
    while Show_Menu:
        Choices = input("1. Update Status \n2. Add A Friend \n3. Send A Message \n4. Read a Message \n0. Exit ")
        if Choices == 1:

            current_status = add_status(current_status)
            print "updated status " + current_status
#use nested if
        elif Choices == 2:

            no_of_friends = add_friend()
            print "you have " + str(no_of_friends) + " friends"
            print "your friend list is: \n" \
                  "" +str(friends)

        elif Choices == 3:
            Send_Message=()



        elif Choices == 0:
            Show_Menu = False
            print "Hope You Enjoyed The Session. \nHave A Good Day..!!"
        else:
            print "Choose A Correct Option."


Existing_Spy = raw_input("Are You A New User (Y/N) ")

if Existing_Spy == "N".lower() or Existing_Spy == "n".upper():
    print "Welcome Back Agent " + Spy['Name'] + ". \nSpy Rating " + str(Spy['Rating']) + "\nAge " + str(Spy['Age'])
    Start_Chat(Spy['Rating'], Spy['Age'])


elif Existing_Spy == "Y".lower() or Existing_Spy == "y".upper():
    Spy ={

        'Name':' ',
        'Age': 0,
        'Rating':0.0
    }
    Spy['Name'] = raw_input("What's Your Name? ")
    if len(Spy['Name']) > 3:
        print "Welcome " + Spy['Name'] + " Glad to see you."

        Spy_Salutation = raw_input("What should we call you (Mr. or Ms.)? ")
        # #use .upper for change alphabet foramt in upper case.

        if Spy_Salutation == "Mr".upper() or Spy_Salutation == "Ms".upper() or \
                        Spy_Salutation == "Mr".lower() or Spy_Salutation == "Ms".lower() or \
                        Spy_Salutation == "Mr".isspace():


            Spy_Name = Spy_Salutation + " " + Spy['Name']

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










