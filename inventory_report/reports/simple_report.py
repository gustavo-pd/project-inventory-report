from collections import Counter


class SimpleReport:

    def generate(products):
        company_names = [item["nome_da_empresa"] for item in products]
        counter = Counter(company_names).most_common(1)

        older_product = sorted(
            products, key=lambda item: item["data_de_fabricacao"]
        )
        older = older_product[0]["data_de_fabricacao"]

        newest_product = sorted(
            products, key=lambda item: item["data_de_validade"]
        )
        newest = newest_product[0]["data_de_validade"]

        return (
          f"Data de fabricação mais antiga: {older}\n"
          f"Data de validade mais próxima: {newest}\n"
          f"Empresa com mais produtos: {counter[0]}"
        )
