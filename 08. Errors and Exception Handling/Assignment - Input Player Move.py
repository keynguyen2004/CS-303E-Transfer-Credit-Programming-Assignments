"""
For this assignment, you might need to think carefully since the
user's input is not always in the correct format/data type that
we expected. Therefore, think of all the possibilities of (incorrect) 
input that the user may entered.


Note: You can reuse the code for the final project, preferrably to 
input human player move. However, it's completely up to you if you
wanted to reuse the code or not (but it is highly recommended given 
our time constraint)

"""


class HumanPlayer:

    def __init__(self, letter):
        super().__init__(letter)  
    

    def getMove(self, game, letter):
        flag = False

        while flag == False:
            square = input(letter + "'s turn. Input move (1 to 9): ")
            try:

                if square.count(".") >= 1 or (square[0] != "-" and 
                                              not square.isnumeric()):
                    raise TypeError
                elif int(square) < 1 or int(square) > 9:
                    raise IndexError
                elif int(square) - 1 not in game.availableMoves():
                    raise ValueError
                else:
                    square = int(square)
                    flag = True

            except TypeError:
                print("Wrong data type. Please try again.")
            except ValueError:
                print("Spot already taken. Please try again.")
            except IndexError:
                print("Invalid option. Please try again.")


        return square


    @staticmethod
    def continueGame():
        flag = False

        while flag == False:
            continueGame = input("Do you want to play another match (Yes/No): ")
            try:

                if not ((continueGame.lower() == "yes") or 
                        (continueGame.lower() == "no")):
                    raise ValueError
                else:
                    flag = True

            except ValueError:
                print("Please enter 'Yes' or 'No' if you want to play another match.")
        

        return continueGame