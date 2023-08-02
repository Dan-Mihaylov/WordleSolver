import json


class DictionaryConverter:

    def __init__(self):
        self.words_dict = {}

    def fill_dictionary_with_data(self, file_path: str):

        with open(f"{file_path}", "r") as file:
            data = json.load(file)
            data = json.loads(data)
        self.words_dict = {item[0]: item[1] for item in data}

        return self.words_dict

    def available_words(self):
        return self.words_dict
