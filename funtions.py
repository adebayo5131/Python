def number():
    print('How many cats do you have')
    numcats= input()
    try:
        
        if int(numcats) > 4:
            print('You have alot')
        else:
            if int(numcats) < 0:
                print('Enter a number greater than 0')
                number()
            else:
                print('you have fewer cats')
        
    except ValueError:
        print('Not a number')


number()

#try and except used to catch errors in a code. Funtion is just like classess
