class WordFinder:

    def __init__(self):
        self._used_words: list = []
        self._letters_not_in_word: list = []
        self._correct_position_letters: dict = {}
        self._wrong_position_letters: dict = {}

    def used_word(self, word: str, *correct_positions: int):
        self._used_words.append(word.lower())

        for index, letter in enumerate(word):
            if letter.islower():
                if (letter not in self._correct_position_letters.values()
                        and letter not in self._wrong_position_letters.values()):

                    self._letters_not_in_word.append(letter)

            elif letter.isupper():
                if correct_positions and index + 1 in correct_positions:
                    self._correct_position_letters[index] = letter.lower()
                    if letter.lower() in self._letters_not_in_word:
                        self._letters_not_in_word.remove(letter.lower())

                else:
                    self._wrong_position_letters[index] = letter.lower()

    def suggest_word(self, available_words: dict) -> list:
        # key == word value = frequency
        # TODO It is already sorted, so no need to check frequencies
        result = []
        for word in available_words:
            candidate = True

            if "'" in word:
                continue

            if self._correct_position_letters:
                for index, letter in self._correct_position_letters.items():
                    if word[index] != letter:
                        candidate = False
                        break

                if not candidate:
                    continue

            if self._wrong_position_letters:

                for index, letter in self._wrong_position_letters.items():
                    if letter in word and word[index] != letter:
                        continue
                    else:
                        candidate = False
                if not candidate:
                    continue

            if self._letters_not_in_word:

                for letter in self._letters_not_in_word:
                    if letter in word:
                        candidate = False
                        break
                if not candidate:
                    continue

            if word in self._used_words:
                continue

            result.append(word)

        if len(result) > 10:
            return result[:11]

        return result
