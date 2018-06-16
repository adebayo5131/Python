import random
import math


class Dice():
    rounds = 3
    round =0
    compDie = 0
    userDie = 0
    compWins = 0;
    userWins = 0;
    tiedGames = 0;


    def rollDice(self):


                for i in range(self.rounds):
                    self.round += 1
                    self.compDie = (random.randint(1, 6))
                    self.userDie = (random.randint(1, 6))

                    print('Computer Die = ' + str(self.compDie) + '\t User Die =' + str(self.userDie))


                    if self.compDie != self.userDie:
                        if self.compDie > self.userDie:
                            print('Computer wins the round' + str(self.round) + '\n')

                        elif self.userDie > self.compDie:
                            print('User wins the round' + str(self.round) + '\n')

                            if self.compDie > self.userDie:
                                self.compWins += 1
                            else:
                                self.userWins += 1



                    else:
                            print('Game was tied\n')
                            self.tiedGames += 1










    def Who_won_more(self):

        if self.compWins > self.userWins:
            print('Computer is the grand winner')
        elif self.userWins > self.compWins:
            print('User is the grand winner')
        else:
            print('The game ended up in a tie')






    def display(self):
        (self.rollDice())
        (self.Who_won_more())


if __name__ == '__main__':
    Dice().display()
