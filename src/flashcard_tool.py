with open("flashcard.csv") as file:

    correct = 0
    questions = 0

    next(file)  # Skips header
    for line in file:
        flashcard = line.strip().split(";")

        answer = input(f"{flashcard[0]}: ")

        if answer.lower() == flashcard[1].lower():
            print("Correct!")
            correct += 1
        else:
            print("Wrong!")
        questions += 1
        print()

    print(f"Your score is {correct}/{questions}")