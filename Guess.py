import random
def guess():
    print('Hello what is your name: ')
    name = input()
    
    print('Well, ' + name +', I am thinking of a number between 1 and 20.')
   
    playOrNot(name)
    
def playOrNot(name):
        
        print('Do you want to take a guess? Yes or No')
        decision = str(input())
        
        target = random.randint(1,20)

        attempts =0
        playerPoints = 0

        try:
              if decision == 'Yes' or decision == 'yes' or decision == 'y':
                  
                    try:
                         for guessTaken in range(1,6):
                            print('Take a guess')
                            guess = int(input())
                            #attempts = attempts +1
                            
                           
                                
                            if  guess > target:
                                print('You guessed too high')
                                
                            elif guess < target :
                                print('You guessed too low')
                                    
                            elif int(guess) == target:
                                
                                print('You guessed the number I am thinking correctly after ' + str(guessTaken)+ ' attempt(s)')
                                print('You have earned ' + str(playerPoints))
                                print('Do you want to play again ?')
                                decison = input()
                                
                                if decision == 'Yes' or decision == 'yes' or decision == 'y':
                                    playOrNot(name)
                                else:
                                    print('Thank you for playing ' + str(name))
                                playerPoints = playerPoints + 1
                                
                                break;
                            else:
                                if int(guess) < 0:
                                    print('Enter a number: ')
                                    guess()
                                    
                         if guessTaken == 5:
                             print('Hey ' + name + ' you have reach the maximum number of guesses.' +
                                   ' The number I was thinking is ' + str(target))
                        
                    except ValueError:
                        print('Not a number')
              elif decision == 'No':
                  print('So sad but the number I was thinking is ' + str(target))
                  
              else:
                  print('A Yes or no answer is requested try again.')
                  playOrNot(name)
                  
                  
                            
        except ValueError:
            print('A "Yes" or no answer is requested try again.')


            
        
       
guess()
