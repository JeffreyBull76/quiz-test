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
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    print(answer)
    # try:
    #     if (A, B, C) in answer:
    #         raise ValueError(
    #             f"Exactly 6 values required, you provided {len(values)}"
    #         )
    # except ValueError as e:
    #     print(f"Invalid data: {e}, please try again.\n")
    #     return False

    # return True


def ask_question():
    """
    Question function
    """
    random_question = randrange(2) + 1
    questions = SHEET.worksheet('questions')

    print(questions.col_values(1)[random_question])
    print(f'A: {questions.col_values(2)[random_question]} \
    B: {questions.col_values(3)[random_question]} \
     C: {questions.col_values(4)[random_question]}')

    answer = input("Enter your answer here:\n")

    validate_question(answer)

    # if validate_question(random_question):
    #         print("Answer is valid!")
    #         break

    # print()
    # return sales_data


ask_question()
