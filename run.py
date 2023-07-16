while True:
    def game_introduction():
        """
        Function to introduce the game and ask the user if they would like to play.
        """
        play_decision = input("Would you like to play? (yes/no)")
        if play_decision.lower().strip() == "yes":
            start_zone()
        else:
            print("Understood, you are not ready for the challenge...")

        
    def start_zone():
        print("hello")
        
    def main_game():
        game_introduction()

    