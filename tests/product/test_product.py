from inventory_report.inventory.product import Product


def test_cria_produto():
    produto = Product(
        3,
        'pasta de dente',
        'Colgate',
        '2022-02-22',
        '2022-07-15',
        '265785',
        'sem especificação',
    )

    assert produto.id == 3
    assert type(produto.id) == int
    assert produto.nome_do_produto == 'pasta de dente'
    assert type(produto.nome_do_produto) == str
    assert produto.nome_da_empresa == 'Colgate'
    assert type(produto.nome_da_empresa) == str
    assert produto.data_de_fabricacao == '2022-02-22'
    assert type(produto.data_de_fabricacao) == str
    assert produto.data_de_validade == '2022-07-15'
    assert type(produto.data_de_validade) == str
    assert produto.numero_de_serie == '265785'
    assert type(produto.numero_de_serie) == str
    assert produto.instrucoes_de_armazenamento == 'sem especificação'
    assert type(produto.instrucoes_de_armazenamento) == str
