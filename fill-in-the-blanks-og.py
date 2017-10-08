import sys

# define all variables of the game here
levels = ["easy", "medium", "hard"]
maxAttempts = 5

textEasy = '''A common first thing to do in a language is display
'Hello __1__!'  In __2__ this is particularly easy; all you have to do
is type in:
__3__ "Hello __1__!"
Of course, that isn't a very useful thing to do. However, it is an
example of how to output to the user using the __3__ command, and
produces a program which does something, so it is useful in that capacity.

It may seem a bit odd to do something in a Turing complete language that
can be done even more easily with an __4__ file in a browser, but it's
a step in learning __2__ syntax, and that's really its purpose.'''
correctEasy = ["world", "python", "print", "html"]
blanksEasy = 4

textMedium = '''A __1__ is created with the def keyword.  You specify the inputs
a __1__ takes by adding __2__ separated by commas between the parentheses.
__1__s by default returns __3__ if you don't specify the value to retrun. __2__
can be standard data types such as string, integer, dictionary, tuple, and __4__
or can be more complicated such as objects and lambda functions.'''
correctMedium = ["function", "arguments", "none", "list"]
blanksMedium = 4

textHard = '''When you create a __1__, certain __2__s are automatically
generated for you if you don't make them manually. These contain multiple
underscores before and after the word defining them.  When you write
a __1__, you almost always include at least the __3__ __2__, defining
variables for when __4__s of the __1__ get made.  Additionally, you generally
want to create a __5__ __2__, which will allow a string representation
of the method to be viewed by other developers.

You can also create binary operators, like __6__ and __7__, which
allow + and - to be used by __4__s of the __1__.  Similarly, __8__,
__9__, and __10__ allow __4__s of the __1__ to be compared
(with <, >, and ==).'''
correctHard = ["class", "method", "answer", "answer", "answer", "answer", "answer", "answer", "answer", "answer"]
blanksHard = 10

# function to print helpful text when game starts based on difficulty level
# takes input of which level user has chosen and predefined fill blanks text
def startingText(levelName, levelText):
    print "You've chosen " + levelName + "!" + "\n"
    print "You will get 5 guesses per problem" "\n"
    print "The current paragraph reads as such:" "\n"
    print levelText
    print "\n"

# function to print wrong answer help text on screen
# takes input of how many tries are left and predefined fill blanks text
def wrongText(triesLeft, levelText):
    print "That isn't the correct answer!  Let's try again; you have " + str(triesLeft-1) + " tries left!" "\n" "\n"
    print "The current paragraph reads as such:" "\n"
    print levelText
    print "\n"

# function which asks for user input
# takes input of which blank number is currently being filled
# retuns the user input which can be used programtically
def userInput(blankNumber):
    value = raw_input("What should be substituted in for __" + str(blankNumber + 1) + "__?\n").lower()
    return value

# function to print correct answer help text on screen
def correctText():
    print "Correct! Correct! Correct!\n \n"
    print "The current paragraph reads as such:\n"

# function which fills in the blank sequentially
# takes input of paragraph text and replaces current blank with correct answer
# returns the replaced text to be used in next iteration
def fillBlank(text, toReplace, withNew):
    newText = text.replace(toReplace, withNew)
    print newText
    print "\n"
    return newText

# function to run the block of code of starting game for each level chosen. Inputs:
# The phrase that should be filled;
# A list with answers that should be verified and compared;
# The number of blanks that should be filled;
def runBlock(levelName, levelText, levelCorrectAnswers, levelBlanks):
    startingText(levelName, levelText) # print starting text for that level
    i = 0
    while (i < levelBlanks): # gets user inputs and stores it
        userI = userInput(i)
        attempts = maxAttempts
        while (userI != levelCorrectAnswers[i]): # check input w/ correct answers
            wrongText(attempts,levelText)
            attempts -= 1
            if (attempts == 0):
                print "You've failed too many straight guesses! Game over!"
                sys.exit()
            userI = userInput(i)
        correctText()
        replaceBlank = "__" + str(i+1) + "__"
        levelText = fillBlank(levelText, replaceBlank, userI)
        i+= 1
        attempts = maxAttempts #reshuffle the attempts number for next blank
    print "You won!"
##############################################################################
# game starts and asks for level from user
print "Choose the right option."
print "Please select a game difficulty by typing it in! \n \n"
userLevel = raw_input("Possible choices include easy, medium, and hard.\n").lower()

# if user inputs unknown level
while userLevel not in levels:
    print "Please choose only from 3 possible levels!"
    print "Please select a game difficulty by typing it in! \n \n"
    userLevel = raw_input("Possible choices include easy, medium, and hard.\n").lower()

# check and proceed for difficulty level choosen by user
if userLevel == levels[0]:
    runBlock(userLevel, textEasy, ["world", "python", "print", "html"], blanksEasy)

elif userLevel == levels[1]:
    runBlock(userLevel, textMedium, ["function", "arguments", "none", "list"], blanksMedium)

elif userLevel == levels[2]:
    runBlock(userLevel, textHard, ["class", "method", "answer", "answer", "answer", "answer", "answer", "answer", "answer", "answer"], blanksHard)
