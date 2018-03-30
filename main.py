from spy_details import spy_name, spy_age, spy_raiting
print 'Hello Buddy'
print 'Let\'s get started'
STATUS_MESSAGE = ['Galti Bade Galti Engineering','Attachment are good for email only','sleepy','all is well','Bhole']


def add_status(c_status):
    if c_status != None:
        print "your current_status is " + c_status
    else:
        print "you dont have any status currently"
    existing_status = raw_input("you want to select from old status? Y/N")
    if existing_status.upper()=="N":
        new_status=raw_input("enter your status " )
        if len(new_status)>0:
            STATUS_MESSAGE.append("new_status")
    elif existing_status.upper()=="Y":
        serial_no = 1
        for old_status in STATUS_MESSAGE:
            print str(serial_no) + " . " +  old_status
            serial_no=serial_no + 1
        user_choice = input ("enter your choice: ")
        new_status =  STATUS_MESSAGE[user_choice-1]
    update_status=new_status
    return update_status





def start_chat(spy_name,spy_age,spy_raiting):
    print "Here are you options "+ spy_name
    current_staus = None
    show_menu= True
    while show_menu:
        choice =  input ("what do want to do? \n 1. Add a status \n 2. Add a friend \n 3.send a message \n 4. Read the message \n 0. exit")
        if choice == 1:
            updated_status_message = add_status(current_status)
            print "updated status is " +  updated_status_message

        elif choice==2:
            print "will add a frnd"
        elif choice==0:
            show_menu = False
        else:
            print "invalid input"

spy_exist = raw_input("Are you a new user? Y/N")
if spy_exist.upper()=="N":      #use nested if & else.
    print "Welcome Back "  +spy_name + " age: "+str(spy_age) +" having raiting of " +str(spy_raiting)

elif spy_exist.upper()=="Y":     #use .upper for change alphabet foramt in upper case.
    spy_name=raw_input('what is your spy name..!!')
    if len(spy_name)>2:
        print  'welcome '  + spy_name +  '. Glad to have you back with us.'
        spy_salution = raw_input("what should we call you(Mr or Ms)?")
        if spy_salution.upper()=="Mr"  or spy_salution.upper()=="Ms":
            spy_name = spy_salution + " "+ spy_name
            print "alright " + spy_name + ". I would like to know a little bit about you"
            spy_age = 0
            spy_raiting = 0.0      #use for known about spy_qualification.
            spy_is_online = True
            spy_age = input('what is your age?')
            if 50>spy_age>12:

                print "your age is correct"
                spy_raiting = input('what is your raiting?')
                if spy_raiting>5.0: #nested if
                     print "great spy"
                elif 3.5<spy_raiting<=5.0:
                    print "avg. spy"
                elif 2.5<spy_raiting<=3.5:
                    print "bad spy"
                else:
                    print " who hired you? "
                spy_is_online = True
                print "Authentication Complete Welcome " + spy_name + " age:" +str(spy_age) + " raiting:"+str(
                    spy_raiting)
            else:
                print "you are not eligible for spy..!!"
        else:
            print "invalid salution"
    else:
        print "ooopss please enter valid name"
else:
    print"invalid entry"





