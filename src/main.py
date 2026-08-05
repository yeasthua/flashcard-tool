FILENAME = "flashcard.csv"

with open(FILENAME) as file:

    correct = 0
    questions = 0
    
    next(file)  # Skips header
    for line in file:

        try:
            question, correct_answer = line.split(";")
            question = question.strip()
            correct_answer = correct_answer.strip()
        except ValueError:  # Skips bad lines
            continue

        answer = input(f"{question}: ")

        if answer.lower() == correct_answer.lower():
            print("Correct!")
            correct += 1
        else:
            print("Wrong!")
        questions += 1
        print()

    print(f"Your score is {correct}/{questions}")