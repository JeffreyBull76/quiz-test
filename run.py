import gspread
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


# def validate_question(answer):
#     """
#     Checks for valid answer
#     """
#     if answer.upper() not in ("A", "B", "C"):
#         print("Answer is not valid!")
#         print("Please answer with A, B or C")
#         return False
#     else:
#         print("Answer is valid!")
#         return True


# def check_question(answer, active_quest):
#     """
#     Checks to see if answer is correct or incorrect
#     """
#     quest = SHEET.worksheet('questions')
#     quest_num = active_quest

#     if answer.upper() == quest.col_values(5)[quest_num]:
#         print("correct")
#     else:
#         print("incorrect")


# def ask_question():
#     """
#     Question function
#     """
#     quest = SHEET.worksheet('questions')
#     quest_num = 1

#     while quest_num <= 5:
#         print(quest.col_values(1)[quest_num])
#         for i in range(2, 5):
#             print(
#                 f"{quest.col_values(i)[0]}: {quest.col_values(i)[quest_num]}"
#                 )

#         answer = input("Enter your answer here:\n")

#         if validate_question(answer):
#             check_question(answer, quest_num)
#             quest_num += 1


que_cat = ['Question', 'Option A', 'Option B', 'Option C', 'Answer']


def set_question():
    """
    Question function
    """
    quest = SHEET.worksheet('questions')
    quest_num = 1

    while quest_num <= 5:
        for i in range(1, 6):
            print(
                f"{quest.col_values(i)[0]}: {quest.col_values(i)[quest_num]}"
                )

        quest_num += 1
            

set_question()


# ask_question()

# loop now correctly checks for a valid answer 
# NEXT we must track and itterate the players score
# THEN write that score to the worksheet with a username

# EXTRA WORK allow selecting difficulty and different categories
# TRY to implement some form of method to show I can use this