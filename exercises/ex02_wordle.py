"""A game that resembles Wordle."""

__author__: str = "730559966"


def contains_char(real_answer: str, char_guess: str) -> bool:
    """Provides the end answer of the function and checks the guesses."""
    assert len(char_guess) == 1, f"len('{char_guess}') is not 1"
    count: int = 0
    while count < len(real_answer):
        if char_guess == real_answer[count]:
            # if guess character is the same as a character in the answer
            return True
        else:
            count = count + 1
            # adds 1 to count
    return False


def emojified(guess: str, secret: str) -> str:
    """Turns guesses into colored boxes corresponding with placement."""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    WHITE_BOX: str = "\U00002B1C"
    # emoji for white box
    GREEN_BOX: str = "\U0001F7E9"
    # emoji for green box
    YELLOW_BOX: str = "\U0001F7E8"
    # emoji for yellow box
    result: str = ""
    count: int = 0
    while count < len(secret):
        if guess[count] == secret[count]:
            # Correct Letter and Placing
            result = result + GREEN_BOX
        elif contains_char(secret, guess[count]) == True:
            # Correct Letter, Incorrect Placing
            result = result + YELLOW_BOX
        else:
            # Incorrect Letter
            result = result + WHITE_BOX
        count += 1
    return result


def input_guess(explength: int) -> str:
    """Takes an expected length value and requests a word of that length until given."""
    given: str = input(f"Enter a {explength} character word:")
    while len(given) != explength:
        given = input(f"That wasn't {explength} characters! Try again:")
        # prompts to give a different length word if it doesn't match explength
    return given
    # returns the given word when it is the correct length


def main(secret_word: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    while turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        # establishes a variable link to the return from input_guess
        main_guess: str = input_guess(explength=len(secret_word))
        print(emojified(guess=main_guess, secret=secret_word))
        # calls emojified to show correct/incorrect guessed letters
        if main_guess == secret_word:
            print(f"You won in {turn}/6 turns!")
            # reflects winning the game if guess=secret
            return
        turn += 1
    print("X/6 - Sorry, try again tomorrow!")
    # reflects losing the game


if __name__ == "__main__":
    main(secret_word="codes")
