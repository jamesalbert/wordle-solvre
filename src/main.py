import nltk
from nltk.corpus import words


def sort_by_common_letters(words):
    letter_freq = dict()
    for word in words:
        for letter in word:
            letter_freq[letter] = letter_freq.get(letter, 0) + 1
    return sorted(words, key=lambda x: sum([letter_freq[letter] for letter in x]))


# standard filtering against specified key
def refine(key):
    global possible_words
    possible_words = list(filter(key, possible_words,))


# refine the list of words based on the state, misplaced, and incorrect letters
def refine_words(state, given, misplaced, incorrect):
    refine(
        lambda x: all([not letter or x[i] == letter for i, letter in enumerate(state)])
    )
    refine(
        lambda x: all(
            [
                letter in x and x.index(letter) != given.index(letter)
                for letter in misplaced
            ]
        )
    )
    refine(lambda x: all([letter not in x for letter in incorrect]))


# get input from the user and return it as a list
def get_input(prompt):
    return list(map(lambda x: x.lower(), list(input(prompt))))


# remove duplicates from list
def remove_duplicates(l):
    return list(dict.fromkeys(l))


# get the difference between two lists
def diff(li1, li2):
    return list(set(li1) - set(li2)) + list(set(li2) - set(li1))


def main():
    global round, max_rounds, max_letters
    state = [str()] * max_letters
    while round < max_rounds:
        misplaced = []
        print(f"\n=== Round {round}/{max_rounds} ===")
        given = get_input("Which letters did you choose?")
        if len(given) != max_letters:
            print(f"Please enter {max_letters} letters.")
            continue
        # given, correct, and incorrect are only relevent to the current state
        correct = get_input("Which letters were in the right place?")
        # misplaced letters accumulate and are removed once they are in the correct position
        misplaced = remove_duplicates(
            misplaced + get_input("Which letters were misplaced?")
        )
        # end the game
        if given == correct:
            print("Nice!")
            break
        # if we guessed some letters correctly
        for letter in correct:
            # track the letter in the state
            state[given.index(letter)] = letter
        # aggregate all the incorrect letters
        incorrect = diff(diff(given, correct), misplaced)
        refine_words(state, given, misplaced, incorrect)
        print(f"# possible words: {len(possible_words)}")
        print(f"some words: {sort_by_common_letters(possible_words)[:15]}")
        if not possible_words:
            print("No possible words!")
            break
        round += 1


if __name__ == "__main__":
    nltk.download("words")
    round = 1
    max_rounds = 6
    max_letters = 5
    possible_words = list(
        map(lambda x: x.lower(), filter(lambda x: len(x) == max_letters, words.words()))
    )
    main()
