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
        if response == "I".lower():
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


area_quest = "false"
perim_quest = "false"
mode = "regular"
quest_answered = 0
quest_wrong = 0
quest_right = 0
quiz_results = []
right_wrong = ""

# Ask the user for number of questions / infinite mode
num_questions = int_check("Hello! How many questions would you like?"
                          " ('i' for infinite): ",
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
while quest_answered < num_questions:

    # Rounds headings (based on mode)
    if mode == "infinite":
        round_heading = f"\n♾️♾️♾️ Question {quest_answered + 1} (Infinite mode) ♾️♾️♾️"
    else:
        round_heading = f"\n3️⃣2️⃣1️⃣ Question {quest_answered + 1} of {num_questions} 1️⃣2️⃣3️⃣"

    print(round_heading)

    #determines the type of question asked
    quest_type = random.randint(1, 2)

    # generate numbers for question
    width = random.randint(low_num, high_num)
    height = random.randint(low_num, high_num)

    # calculate answers
    area = width * height
    perimeter = 2 * (width + height)


    #sorts type of question given
    if quest_type == 1:
        area_quest = "true"
        perim_quest = "false"
    elif quest_type == 2:
        perim_quest = "true"
        area_quest = "false"

    #testing remove when done
    print("area", area)
    print("perimeter", perimeter)

    # makes infinite mode infinite
    if mode == "infinite":
        num_questions += 1


    # determine type of question and whether it is correct
    if area_quest == "true":

        #asks question,
        user_ans = (int_check(f"if the width is {width} and the height is {height}"
                        f" What is the area? ", exit_code="xxx"))

        # checks if user is correct
        if user_ans == area:
            quest_right += 1
            right_wrong = "right"

        #allows user to exit quiz
        elif user_ans == "xxx":
            print("\nYou left :(")
            break

        #checks if user is wrong
        else:
            quest_wrong += 1
            right_wrong = "wrong"


        quest_results = f" At question {quest_answered + 1} you answered {user_ans} the answer was {area} you were {right_wrong}\n"
        print(quest_results)

        # make questions progress
        quest_answered += 1

        quiz_results.append(quest_results)

    # determine type of question and whether it is correct
    elif perim_quest == "true":

        user_ans = (int_check(f"if the width is {width} and the height is {height}"
                        f" What is the perimeter? ", exit_code="xxx"))

        # checks if user is correct
        if user_ans == perimeter:
            quest_right += 1
            right_wrong = "right"

        #allows user to exit quiz
        elif user_ans == "xxx":
            print("\nYou left :(")
            break

        #checks if user is wrong
        else:
            quest_wrong += 1
            # determines if question is wrong
            right_wrong = "wrong"


        quest_results = f" At question {quest_answered + 1} you answered {user_ans} the answer was {perimeter} you were {right_wrong}\n"
        print(quest_results)

        # make questions progress
        quest_answered += 1

        quiz_results.append(quest_results)

print("\nAll done pal (。・ω・。)\n")

#check is user wants to see quiz history
want_end_result = string_checker("❔❓❔Would you like to see how you did?❓❔❓ ")

if want_end_result == "yes":

    print("\n✨✨Quiz Results✨✨\n")

    for item in quiz_results:
        print(item)

    print(f"Summary: You got {quest_right} questions right"
          f" and {quest_wrong} questions wrong.")

print("\nHave a lovely day!")

