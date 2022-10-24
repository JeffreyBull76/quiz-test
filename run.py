import gspread
from random import randrange
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('python_quiz_questions')


print("WELCOME TO THE QUIZ - ANSWER EACH QUESTION TO PROCEED !\n")
print("Your answers are given by selecting the letter for each choice")
print("So you if you think the answer is B you would type B")


def validate_question(answer):
    """
    Checks for valid answer
    """
    if answer not in ("a", "A", "b", "B", "c", "C"):
        print("Answer is not valid!")
        print("Please answer with A, B or C")
        return False
    else:
        print("Answer is valid!")
        return True


def ask_question():
    """
    Question function
    """
    random_question = randrange(2) + 1
    quest = SHEET.worksheet('questions')

    print(quest.col_values(1)[random_question])
    for i in range(2, 5):
        print(
            f"{quest.col_values(i)[0]}: {quest.col_values(i)[random_question]}"
            )

    answer = input("Enter your answer here:\n")

    if validate_question(answer):
        print(answer)
    else:
        answer = input("Enter your answer here:\n")
        # The above functionality works but needs to be a while loop (CAUTION)


ask_question()

# Next we need to make sure this call loops to request a valid answer
# Also need to make a function that generates 4 or 5 uniques numbers for asking
# the questions this will replace or become the random question var

# Further work we need to score the player - try to create a method for 
# this that calls whenever a question is asked 
