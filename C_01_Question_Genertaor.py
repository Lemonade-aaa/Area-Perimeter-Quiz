import random


# # checks user enters yes (y) or no (n)
def string_checker(question, valid_ans=('yes', 'no')):

    error = f"Please enter a valid option from the following list {valid_ans}"

    while True:

        #get user response and make sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            #check if the user response is a word in the list
            if item == user_response:
                return item

            #check if the user response is the same as
            #the first letter of an item on the list
            elif user_response == item[0]:
                return item

        # print error if user does not enter something that is valid
        print(error)
        print()


# checks for an integer with optional upper /
# lower limits and optional exit code for infinite mode
# / quitting the game
def int_check(question, low=None, high=None, exit_code=None,):


    # if any integer is allowed...
    if low is None and high is None:
        error = "please enter an integer"

    # if larger number needs to be more than an
    # integer (ie: rounds / 'high number')
    elif low is not None and high is None:
        error = (f"Please enter and integer that is "
                 f"more than / equal to {low}")

    # if the number needs to be between low & high
    else:
        error = (f"Please enter a integer that "
                 f"is between {low} and {high} (inclusive)")

    while True:
        response = input(question).lower()

        # check for infinite mode
        if response == "":
            return "infinite"

        #check for infinite mode / exit code
        if response == exit_code:
            return response

        try:
            response = int(response)

            #check the integer is not too low
            if low is not None and response < low:
                print(error)

            #check response is more than low number
            elif high is not None and response > high:
                print(error)

            #if response is valid, return it
            else:
                return response

        except ValueError:
            print(error)


mode = "regular"
rounds_played = 0
loop = "true"

# Ask the user for number of rounds / infinite mode
num_rounds = int_check("Hello! How many questions would you like?: ",
                       low=1, exit_code="")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5


# ask user if they want to customise the number range
default_params = string_checker("Do you want the default height and width (1, 10)? ")
if default_params == "yes":
    low_num = 1
    high_num = 10

# Allow user to choose the high / low number
else:
    low_num = int_check("What would you like as the minimum? ")
    high_num = int_check("what would you like as the maximum? ", low=low_num + 1)

# Game loop starts here
while rounds_played < num_rounds:

    # Rounds headings (based on mode)
    if mode == "infinite":
        round_heading = f"\n♾️♾️♾️ Question {rounds_played + 1} (Infinite mode) ♾️♾️♾️"
    else:
        round_heading = f"\n3️⃣2️⃣1️⃣ Question {rounds_played + 1} of {num_rounds} 1️⃣2️⃣3️⃣"

    print(round_heading)


    #guess loop
    while loop == "true":

        #generate numbers for question
        width = random.randint(low_num,high_num)
        height = random.randint(low_num,high_num)

        #calculate answers
        area = width * height
        perimeter = 2 * (width + height)

        #testing remove when done
        print(area)
        print(perimeter)


        #print question
        area_guess = int_check(f"If the width is {width} height is {height} what is the area: ")

        if area_guess == area:
            print("you are correct")
        else:
            print("WRONG")

        perimeter_guess = int_check(f"Using the same numbers what is the perimeter: ")

        if perimeter_guess == perimeter:
            print("correct")
        else:
            print("WRONG")

        # make round progress
        rounds_played += 1


