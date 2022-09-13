from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):

    def generate(products):

        simple_report = SimpleReport.generate(products)
        stock = ''

        company_names = [item["nome_da_empresa"] for item in products]
        counter = Counter(company_names).most_common()

        for key, value in counter:
            stock += f"- {key}: {value}\n"

        return (
            f"{simple_report}\n"
            "Produtos estocados por empresa:\n"
            f"{stock}"
        )
