from dictionary_converter import DictionaryConverter
from words import WordFinder


class Game:

    def __init__(self):
        self._available_words = {}
        self.finder = WordFinder()
        self._fill_available_words()
        self.play()

    def _fill_available_words(self):
        dictionary = DictionaryConverter()
        dictionary.fill_dictionary_with_data("words.json")
        self._available_words = dictionary.available_words()

    def play(self):
        print(
            f"--- FIND WORDS FOR WORDLE GAME --------------------------------------\n"
            f"--- RULES: ----------------------------------------------------------\n"
            f"--- TYPE THE WORD YOU HAVE ALREADY INSERTED, OR IF IT IS YOUR FIRST -\n"
            f"--- WORD TYPE SUGGEST FOR A SUGGESTION. -----------------------------\n"
            f"--- UPPERCASE LETTER MEANS THE LETTER IS IN THE WORD ----------------\n"
            f"--- A LOWERCASE MEANS IT ISN'T --------------------------------------\n"
            f"--- WHEN ASKED ABOUT THE CORRECT POSITION OF THE LETTER -------------\n"
            f"--- IF YOU HAVE ANY, TYPE THEM SEPARATED BY SPACE (' ') -------------\n"
        )

        first_word = True

        while True:
            if first_word:
                user_word = input(f"Enter Word or type Suggest for first word suggestions -> \n")
                first_word = False
                if user_word.lower() == "suggest":
                    print(f"{self._suggest_first_word()}\n")
                    continue
            else:
                user_word = input(f"Enter Word -> \n")

            user_correct_pos = input(f"Enter Correct Positions Separated By Comma and Space -> \n")

            positions = []
            if user_correct_pos.strip() != "":
                positions = user_correct_pos.split()
                positions = [int(x) for x in positions]

            self.finder.used_word(user_word, *positions)
            results = self.finder.suggest_word(self._available_words)
            print(", ".join(results))

            command = input("\nEnter To Continue / Q to Quit / New for new game -> \n")
            if command.lower() == "q":
                break
            elif command.lower() == "new":
                print("New Game Starting, Words Have Reset\n")
                first_word = True
                self._new_game()

        print("Thanks For Cheating! ")

    def _new_game(self):
        self.finder = WordFinder()

    def _suggest_first_word(self):
        result = []
        counter = 0

        for word in self._available_words:
            if "'" not in word:
                result.append(word)
            else:
                continue

            counter += 1

            if counter == 20:
                return f", ".join(result[1:])


if __name__ == "__main__":
    Game()

