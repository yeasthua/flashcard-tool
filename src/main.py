import random # For shuffling flashcards

def read_file(filename: str) -> list[list]:
    "Reads the flashcard file, and then returns a list of lists which contains each line in the file (except header)"
    
    with open(filename, "r") as file:
        rows = []
        next(file)  # Skips header
    
        # Appends each question and answers into rows
        for line in file:
            if line == "":  # Skips line that is empty
                continue
    
            try:
                rows.append(line.strip().split(";"))
            except ValueError:  # Skips lines that has incorrect format
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
            print("[Correct]\n")
            correct += 1
        else:
            print("[Incorrect]\n")

    print(f"Total score: {correct}/{len(questions_and_answers)}")

def write_flashcards():
    filename = input("Enter new filename (.csv only): ")
    if ".csv" not in filename:  # If file extension is not .csv
        raise TypeError
    
    cards = []
    cards.append("Question;Answer\n")     # Add header to flashcard

    print("==== WRITE FLASHCARD  ====")
    print("    Input '1' to exit   \n")
    while True:
        question = input("Question: ")
        if question == '1':
            break 

        answer = input("Answer: ")
        if answer == '1':
            break
        print()

        cards.append(f"{question};{answer}\n")

    return filename, cards

def create_file(filename: str, cards: list):
    "Creates a new flashcard file using the contents of the given list"

    with open(filename, "w") as file:
        for line in cards:
            file.write(line)

def delete_contents(filename: str):
    "Deletes all contents of the given filename"
    if ".csv" not in filename:
        raise TypeError

    with open(filename, "w") as file:
        pass

    print("STATUS: All contents erased!")


def main():
    print("""
    ╱╭━┳╮╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╭╮╱╱╭╮╱╱╱╱╱╱╭╮
    ╱┃╭┫┃╱╱╱╱╱╱┃┃╱╱╱╱╱╱╱╱╱╱╱┃┃╱╭╯╰╮╱╱╱╱╱┃┃
    ╭╯╰┫┃╭━━┳━━┫╰━┳━━┳━━┳━┳━╯┃╱╰╮╭╋━━┳━━┫┃
    ╰╮╭┫┃┃╭╮┃━━┫╭╮┃╭━┫╭╮┃╭┫╭╮┣━━┫┃┃╭╮┃╭╮┃┃
    ╱┃┃┃╰┫╭╮┣━━┃┃┃┃╰━┫╭╮┃┃┃╰╯┣━━┫╰┫╰╯┃╰╯┃╰╮
    ╱╰╯╰━┻╯╰┻━━┻╯╰┻━━┻╯╰┻╯╰━━╯╱╱╰━┻━━┻━━┻━╯
                                by yeasthua
    """)

    while True:
        #* Main menu
        print("""
        ========== FUNCTIONS ==========
        (1): Run flashcard program
        (2): Create a new flashcard file
        (3): Erase all contents of an existing flashcard file
        (4): Exit program
        """)

        # Handles invalid function input, eg: str or > 4
        try:
            user_input = int(input("Enter function: "))
        except ValueError:
            print("ERROR: Invalid Input\n")
            continue
        if user_input > 4 or user_input < 1:
            print("ERROR: 1-4 only\n")
            continue

        #* Function 1
        if user_input == 1:
            print("====== FLASHCARD ======")
            filename = input("Enter which file would you like to use (.csv files only): ")

            try:
                run_quiz(filename)
            except FileNotFoundError:
                print("ERROR: File not found")

        #* Function 2
        elif user_input == 2:
            try:
                file_name, flashcards = write_flashcards()
                create_file(file_name, flashcards)
            except TypeError:
                print("ERROR: Invalid file extension")
            except OSError:
                print("ERROR: Cannot create file [Invalid filename]")

        #* Function 3
        elif user_input == 3:
            print("==== ERASE CONTENTS ====")
            try:
                filename_delete = input("Enter filename to erase all content: ")
                delete_contents(filename_delete)
            except TypeError:
                print("ERROR: Invalid file extension")
            except OSError:
                print("ERROR: Invalid filename")

        #* Function 4
        elif user_input == 4:
            print("Terminating program...")
            break
    
main()