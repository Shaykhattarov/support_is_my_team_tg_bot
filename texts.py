import os
import json


class Text:
    __filename: str = 'data.json'
    welcome_text: str = 'Привет'

    def __init__(self):
        self.welcome_text = self.read_json_file(self.__filename)["answer1"]["text"]

    @staticmethod
    def read_json_file(filename='data.json') -> dict:
        if filename in os.listdir(os.path.join(__file__)):
            with open(os.path.join(__file__, filename), 'r') as file:
                data = json.loads(file.read())
        else:
            data: dict = {}
            data['answer1']['text'] = "Текст не найден!"
            with open(os.path.join(__file__, filename), 'x') as file:
                json.dumps(obj=data, fp=file)
        return data


