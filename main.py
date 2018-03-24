print"hello"
print 'Let\a get started'
spy_name=raw_input('what is your spy name..!!')

if len(spy_name)>2:
    print  'welcome '  + spy_name +  '. Glad to have you back with us.'
    spy_salution = raw_input("what should we call you(Mr. or Ms.)?")
    if spy_salution=="Mr."  or spy_salution=="Ms.":

        spy_name = spy_salution + "" + spy_name
        print "alright " + spy_name + ". I would like to know a little bit about you"
        spy_age = 0
        spy_raiting = 0.0
        spy_is_online = True
        spy_age = input('what is your age?')
        if 50>spy_age>12:
            print "your age is correct"
            spy_raiting = input('what is your raiting?')
            if spy_raiting>5.0:
                print "great spy"
            elif 3.5<spy_raiting<=5.0:
                print "avg. spy"
            elif 2.5<spy_raiting<=3.5:
                print "bad spy"
            else:
                print " who hired you? "
        else:
            print "you are not eligible for spy..!!"
    else:
        print "invalid salution"

else:
    "oopss please..! enter a valid name"





