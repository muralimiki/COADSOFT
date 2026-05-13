import json

class Storage:
    FILE_NAME = "tasks.json"

    @staticmethod
    def save(tasks):
        with open(Storage.FILE_NAME, "w") as file:
            json.dump([task.to_dict() for task in tasks], file, indent=4)

    @staticmethod
    def load():
        try:
            with open(Storage.FILE_NAME, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []