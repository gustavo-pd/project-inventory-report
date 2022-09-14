from .importer import Importer
import json


class JsonImporter(Importer):
    def import_data(path):
        if path.endswith('.json'):
            with open(path, 'r') as file:
                file_json = json.load(file)
                return file_json
        else:
            raise ValueError("Arquivo inválido")
