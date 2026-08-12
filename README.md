# flashcard-tool

A simple command-line flashcard quiz written in Python.

The program reads flashcards from a file, asks each question, checks the user's answers, and displays the final score.

## Features

- Read flashcards from a `.csv` file
- Ask questions one by one in random order
- Case-insensitive answer checking
- Skip malformed lines in the flashcard file
- Display the final 
- Create a new flashcard file
- Delete the contents of a file

## .csv Format
```bash
Question;Answer
```

## How to run
```bash
git clone https://github.com/yeasthua/flashcard_tool
cd flashcard_tool
python main.py
```
