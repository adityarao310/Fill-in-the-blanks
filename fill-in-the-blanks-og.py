##############################################################################
# define all variables of the game here
levels = ["easy", "medium", "hard"]
attempts = 5

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

textMedium = '''A __1__ is created with the def keyword.  You specify the inputs
a __1__ takes by adding __2__ separated by commas between the parentheses.
__1__s by default returns __3__ if you don't specify the value to retrun. __2__
can be standard data types such as string, integer, dictionary, tuple, and __4__
or can be more complicated such as objects and lambda functions.'''
correctMedium = ["function", "arguments", "none", "list"]

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

# function to print helpful text when game starts based on difficulty level
def startingText(levelName, levelText):
    print "You've chosen " + levelName + "!" + "\n"
    print "You will get 5 guesses per problem" "\n"
    print "The current paragraph reads as such:" "\n"
    print levelText
    print "\n"

# function to print wrong answer help text on screen
def wrongText(triesLeft, levelText):
    print "That isn't the correct answer!  Let's try again; you have " + str(triesLeft) + " tries left!" "\n" "\n"
    print "The current paragraph reads as such:" "\n"
    print levelText
    print "\n"

# function which asks for user input
def userInput(blankNumber):
    value = raw_input("What should be substituted in for __" + str(blankNumber + 1) + "__?" "\n").lower()
    return value

# function to print correct answer help text on screen
def correctText():
    print "Correct! Correct! Correct!" "\n" "\n"
    print "The current paragraph reads as such:" "\n"

# function which fills in the blank sequentially
def fillBlank(text, toReplace, withNew):
    newText = text.replace(toReplace, withNew)
    print newText
    print "\n"
    return newText

##############################################################################
# game starts
print "Please select a game difficulty by typing it in!" "\n"
userLevel = raw_input("Possible choices include easy, medium, and hard.\n").lower()

# check for difficulty level choosen by user
if userLevel in levels:
    if userLevel == levels[1]:
        # print starting text for that difficulty level
        startingText(userLevel, textMedium)

        # get input for 1st blank
        user0 = userInput(0)
        while (user0 != correctMedium[0]):
            wrongText(attempts,textMedium)
            user0 = userInput(0)
        if  user0 == correctMedium[0]:
            correctText()
            textMedium = fillBlank(textMedium, "__1__", user0)

        # get input for 2nd blank
        user1 = userInput(1)
        while (user1 != correctMedium[1]):
            wrongText(attempts,textMedium)
            user1 = userInput(1)
        if  user1 == correctMedium[1]:
            correctText()
            textMedium = fillBlank(textMedium, "__2__", user1)


# if user inputs unknown level
else:
    print "That's not an option!"
    print "Please select a game difficulty by typing it in!"
