from inventory_report.inventory.product import Product


def test_relatorio_produto():
    produto = Product(
        3,
        'pasta de dente',
        'Colgate',
        '2022-02-22',
        '2022-07-15',
        '265785',
        'sem especificação',
    )

    produto_repr = produto.__repr__()

    expected = (
        "O produto pasta de dente"
        " fabricado em 2022-02-22"
        " por Colgate com validade"
        " até 2022-07-15"
        " precisa ser armazenado sem especificação."
    )

    assert produto_repr == expected
