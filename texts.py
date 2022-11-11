import os
import json


class Text:
    __filename: str = 'data.json'
    welcome_text: str

    def __init__(self):
        self.welcome_text = self.read_json_file()["welcome_text"]["text"]

    @staticmethod
    def read_json_file(filename='data.json') -> dict:
        with open(os.path.join(__file__, filename), 'r') as file:
            data = json.loads(file.read())
        return data
