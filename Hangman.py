name = input("Name: ")

print(f"Hello {name} time to play hangman")

secret_word = "secret"

guess_str = ""

lifes = 10

while lifes>0:
    character_left = 0

    for character in secret_word:
        if character in guess_str:
            print(character)
        else:
            print("?")
            character_left += 1
    if character_left ==0:
        print("You won")
        break

    guess = input("Guess a letter: ")
    guess_str += guess

    if guess not in secret_word:
        lifes -= 1
        print("try again")
        print(f" you have a {lifes} left")

        if lifes == 0:
            print("You died")
