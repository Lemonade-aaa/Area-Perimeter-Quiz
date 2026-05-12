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

# #picks whether question will be area based or perimeter based
# def generator(quest_type):
#
#     quest_type = "would you prefer area, perimeter questions or both(press <enter>)? "
#     if quest_type == "":
#
#         quest_type = random.randint(1,2)
#
#         if quest_type == 1:
#             area_quest = "true"
#
#         elif quest_type == 2:
#             perim_quest = "true"


area_quest = "false"
perim_quest = "false"
mode = "regular"
questions_answered = 0
roller = random.randint(1,2)

# Ask the user for number of questions / infinite mode
num_questions = int_check("Hello! How many questions would you like?: ",
                          low=1)

if num_questions == "infinite":
    mode = "infinite"
    num_questions = 5


# ask user if they want to customise the number range
default_params = string_checker("Do you want the default height and width (this will pick a random number between 1 & 10)? ")
if default_params == "yes":
    low_num = 1
    high_num = 10

# Allow user to choose the high / low number
else:
    low_num = int_check("What would you like as the minimum? ")
    high_num = int_check("what would you like as the maximum? ", low=low_num + 1)

# Game loop starts here
while questions_answered < num_questions:

    # Rounds headings (based on mode)
    if mode == "infinite":
        round_heading = f"\n♾️♾️♾️ Question {questions_answered + 1} (Infinite mode) ♾️♾️♾️"
    else:
        round_heading = f"\n3️⃣2️⃣1️⃣ Question {questions_answered + 1} of {num_questions} 1️⃣2️⃣3️⃣"

    print(round_heading)

    roller = random.randint(1, 2)

    # generate numbers for question
    width = random.randint(low_num, high_num)
    height = random.randint(low_num, high_num)

    # calculate answers
    area = width * height
    perimeter = 2 * (width + height)


    if roller == 1:
        area_quest = "true"
        perim_quest = "false"
    elif roller == 2:
        perim_quest = "true"
        area_quest = "false"

    #testing remove when done
    print("area", area)
    print("perimeter", perimeter)


    # determine type of question and whether it is correct
    if area_quest == "true":
        user_ans = (int_check(f"if the width is {width} and the height is {height}"
                        f" What is the area? ", exit_code="xxx"))
        print(user_ans)

        if user_ans == area:
            print("correct")

        #allows user to exit quiz
        elif user_ans == "xxx":
            print("You left :(")
            break



        else:
            print("wrong")

        # make rounds progress
        questions_answered += 1

    elif perim_quest == "true":
        user_ans = (int_check(f"if the width is {width} and the height is {height}"
                        f" What is the perimeter? ", exit_code="xxx"))
        print(user_ans)

        if user_ans == perimeter:
            print("correct")

        #allows user to exit quiz
        elif user_ans == "xxx":
            print("You left :(")
            break

        else:
            print("wrong")


        # make round progress
        questions_answered += 1

        if mode == "infinite":
            num_questions += 1


