import json

class Storage:
    FILE_NAME = "contacts.json"

    @staticmethod
    def save(contacts):
        with open(Storage.FILE_NAME, "w") as file:
            json.dump([contact.to_dict() for contact in contacts], file, indent=4)

    @staticmethod
    def load():
        try:
            with open(Storage.FILE_NAME, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []