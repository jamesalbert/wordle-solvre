import nltk
from nltk.corpus import words

nltk.download("words")

five_letter_words = list(filter(lambda x: len(x) == 5, words.words()))
history = []
state = [str()] * 5
misplaced = []


def diff(li1, li2):
    return list(set(li1) - set(li2)) + list(set(li2) - set(li1))


def refine_words(given):
    global five_letter_words
    five_letter_words = list(
        filter(
            lambda x: all(
                [not letter or x[i] == letter for i, letter in enumerate(state)]
            ),
            five_letter_words,
        )
    )
    five_letter_words = list(
        filter(
            lambda x: all(
                [
                    letter in x and x.index(letter) != given.index(letter)
                    for letter in misplaced
                ]
            ),
            five_letter_words,
        )
    )
    five_letter_words = list(
        filter(
            lambda x: all([letter not in x for letter in incorrect]), five_letter_words
        )
    )


def get_input(prompt):
    return list(map(lambda x: x.lower(), list(input(prompt))))


while True:
    given = get_input("Which letters did you choose?")
    if len(given) != 5:
        print("Please enter 5 letters.")
        continue
    correct = get_input("Which letters were in the right place?")
    misplaced += get_input("Which letters were misplaced?")
    history.append(given)
    if given == correct:
        print("Nice!")
        break
    for letter in correct:
        if letter in misplaced:
            misplaced.remove(letter)
        state[given.index(letter)] = letter
        print(f"new state: {state}")
    incorrect = diff(diff(given, correct), misplaced)
    refine_words(given)
    print(f"# possible words: {len(five_letter_words)}")
    print(f"some words: {five_letter_words[:15]}")
