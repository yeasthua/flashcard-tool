import random # For shuffling questions

def read_file(filename: str) -> list[list]:
    "Reads the flashcard file, and then returns a list of lists which contains each line in the file (except header)"

    with open(filename) as file:
        rows = []
        next(file)  # Skips header
    
        # Appends each question and answers into rows
        for line in file:
    
            try:
                rows.append(line.strip().split(";"))
            except ValueError:  # Skips bad lines
                continue
    return rows

def run_quiz(filename: str):
    """
    Asks the user for an answer to each question based on the file,
    evaluates each answer if they are correct or incorrect,
    and display the total score
    """
    questions_and_answers = read_file(filename)
    random.shuffle(questions_and_answers)   # Shuffles the flashcards

    print("\n==== QUIZ START ====")
    correct = 0
    card_num = 1

    for item in questions_and_answers:
        question, correct_answer = item     # Unpacks the list

        print(f"card {card_num} / {len(questions_and_answers)}")
        user_answer = input(f"{question}: ")
        card_num += 1

        if user_answer.lower() == correct_answer.lower():
            print("Correct!\n")
            correct += 1
        else:
            print("Incorrect\n")

    print(f"You scored {correct}/{len(questions_and_answers)}")


def main():
    print("""
    ╱╭━┳╮╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╭╮╱╱╭╮╱╱╱╱╱╱╭╮
    ╱┃╭┫┃╱╱╱╱╱╱┃┃╱╱╱╱╱╱╱╱╱╱╱┃┃╱╭╯╰╮╱╱╱╱╱┃┃
    ╭╯╰┫┃╭━━┳━━┫╰━┳━━┳━━┳━┳━╯┃╱╰╮╭╋━━┳━━┫┃
    ╰╮╭┫┃┃╭╮┃━━┫╭╮┃╭━┫╭╮┃╭┫╭╮┣━━┫┃┃╭╮┃╭╮┃┃
    ╱┃┃┃╰┫╭╮┣━━┃┃┃┃╰━┫╭╮┃┃┃╰╯┣━━┫╰┫╰╯┃╰╯┃╰╮
    ╱╰╯╰━┻╯╰┻━━┻╯╰┻━━┻╯╰┻╯╰━━╯╱╱╰━┻━━┻━━┻━╯
                                by yeasthua\n
    """)

    while True:
        filename = input("+ Enter which file would you like to use (.csv files only): ")

        try:
            run_quiz(filename)
            break
        except FileNotFoundError:
            print("File not found, please try again.\n")
            continue
    

main()