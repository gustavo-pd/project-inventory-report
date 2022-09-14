from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.complete_report import CompleteReport

report = [
    {
        "nome_da_empresa": "Adidas",
        "data_de_fabricacao": "2020-05-07",
        "data_de_validade": "2033-03-03",
    }
]


def test_decorar_report():
    rep = ColoredReport(CompleteReport).generate(report)
    assert "\033[32mData de fabricação mais antiga:\033[0m" in rep
    assert "\033[31mAdidas\033[0m" in rep
