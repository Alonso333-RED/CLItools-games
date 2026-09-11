from game import Game
import utils
import random


class NumberGuessing(Game):
    name = "Number Guessing"
    description = "Adivina el número secreto"

    def play(self):
        utils.clear_screen()

        secret = random.randint(1, 100)
        attempts = 0

        print("=== NUMBER GUESSING ===")
        print("Estoy pensando un número entre 1 y 100.")

        while True:
            guess = utils.insert_int(
                "Tu intento",
                1,
                1,
                100,
                False
            )

            attempts += 1

            if guess < secret:
                print("Demasiado bajo.")

            elif guess > secret:
                print("Demasiado alto.")

            else:
                print(f"\n¡Correcto!")
                print(f"Intentos: {attempts}")
                input("\nPresiona Enter para continuar...")
                return