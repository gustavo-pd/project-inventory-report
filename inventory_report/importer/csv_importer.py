from .importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(path):
        if path.endswith('.csv'):
            with open(path, 'r') as file:
                file_csv = list(csv.DictReader(file, delimiter=",", quotechar='"'))
                return file_csv
        else:
            raise ValueError("Arquivo inválido")
