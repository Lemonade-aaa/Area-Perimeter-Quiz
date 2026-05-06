


# checks user enters yes (y) or no (n)
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

def instructions():
    """Print instructions"""

    print("""
***INSTRUCTIONS***

Do math
you will be given the width and height, calculate the perimeter and area.
Area calc = width x height.
Perimeter calc = height + width x 2.

Have fun :)

    """)






want_instructions = string_checker("Do you wish to see the instructions? ").lower()

#checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()

