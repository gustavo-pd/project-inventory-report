from .importer import Importer
import xmltodict


class XmlImporter(Importer):
    def import_data(path):
        if path.endswith('.xml'):
            with open(path, 'r') as file:
                file_read = file.read()
                file_xml = xmltodict.parse(file_read)
                return file_xml['dataset']['record']
        else:
            raise ValueError("Arquivo inválido")
