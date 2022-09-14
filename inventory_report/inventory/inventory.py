from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.importer.json_importer import JsonImporter


class Inventory:
    def read(path):
        if "csv" in path:
            return CsvImporter.import_data(path)
        if "xml" in path:
            return XmlImporter.import_data(path)
        if "json" in path:
            return JsonImporter.import_data(path)

    def import_data(path, type_inv):
        file_data = Inventory.read(path)

        if type_inv == "simples":
            return SimpleReport.generate(file_data)
        if type_inv == "completo":
            return CompleteReport.generate(file_data)
