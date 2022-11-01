"""
SAVED TO REFLECT ORIGINAL MODULE FILE IN CI PROJECT 3
"""
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
PLYR_SCORE = 0
"""
Onload text and define global list that holds the questions chosen
"""
print("Your answers are given by selecting the letter for each choice")
print("So you if you think the answer is B you would type B\n")


def set_questions():
    """
    Question function
    """
    get_quest = SHEET.worksheet(f'{CHOS_CAT}').get_all_values()
    return get_quest


q_l = set_questions()


def validate_question(answer):
    """
    Checks for valid answer
    """
    if answer.upper() not in ("A", "B", "C"):
        print("\033[0;37;41mANSWER IS NOT VALID !\033[0;37;48m")
        print("Please answer with A, B or C !")
        return False
    else:
        print("Answer is valid!\n")
        return True


def check_question(answer, rng1, rng2):
    """
    Checks to see if answer is correct or incorrect
    """
    global PLYR_SCORE
    if answer.upper() == q_l[rng2][4]:
        print("CORRECT !\n")
        PLYR_SCORE += 1
    else:
        print("INCORRECT !\n")

    play_game(rng1, rng2 + 1)


def ask_question(rng1, rng2):
    """
    Question function
    """
    quest_cnt = 1

    while quest_cnt < 2:
        for i in range(0, 4):
            print(f"\033[1;34;40m{q_l[rng1][i]}:\033[0;37;48m {q_l[rng2][i]}")

        answer = input("\033[1;32;40mEnter answer here:\033[0;37;48m\n")

        if validate_question(answer):
            check_question(answer, rng1, rng2)
            quest_cnt += 1


def game_over():
    """
    end game and save score function
    """
    print(f"Your score was {PLYR_SCORE}/{len(q_l)}")
    print("GAME OVER!\n")
    name_val = 1

    while name_val < 2:
        def remove(play_name):
            return play_name.replace(" ", "")

        play_name = input("ENTER YOUR NAME TO SAVE YOUR SCORE\n")
        ply_nam = remove(play_name)

        if ply_nam and len(ply_nam) >= 5:
            str1 = ply_nam
            str2 = PLYR_SCORE
            final_str = f'{str1} ' + f'{str2}'
            final_score = list(final_str.split(" "))
            score_value = SHEET.worksheet("scores")
            score_value.append_row(final_score)
            name_val += 1
        else:
            print("\033[0;37;41mEnter a valid name...\033[0;37;48m")
            print("\033[0;37;41mNo blankspaces allowed...\033[0;37;48m")
            print("\033[0;37;41mMinimum 5 characters !\033[0;37;48m\n")


def play_game(val1, val2):
    """
    Allows iteration through different questions sequences
    """
    print("\033[1;32;40mSCORE = " + f'{PLYR_SCORE}\033[0;37;48m')
    if val2 < 11:
        ask_question(val1, val2)
    else:
        # sys.exit("GAME OVER!")
        game_over()
        # exec(open("run.py").read())


play_game(0, 1)
