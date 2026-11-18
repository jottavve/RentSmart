
from imovel import Imovel
from orcamento import Orcamento
from gerador_csv import GeradorCSV


def solicitar_tipo_imovel():
    while True:
        print("\nTIPOS DE IMÓVEIS")
        print("1 - Apartamento")
        print("2 - Casa")
        print("3 - Estúdio")

        opcao = input("Escolha o tipo de imóvel: ")

        tipos = {
            "1": "Apartamento",
            "2": "Casa",
            "3": "Estúdio"
        }

        if opcao in tipos:
            return tipos[opcao]

        print("Opção inválida! Tente novamente.")


def solicitar_quartos(tipo):
    if tipo == "Estúdio":
        return 0

    while True:
        try:
            quartos = int(input("Quantos quartos? (1 ou 2): "))

            if quartos in [1, 2]:
                return quartos

            print("Escolha apenas 1 ou 2 quartos.")

        except ValueError:
            print("Digite um número válido.")


def solicitar_vagas(tipo):
    if tipo in ["Apartamento", "Casa"]:
        while True:
            try:
                vagas = int(input("Possui vaga de garagem? (0 = Não / 1 = Sim): "))

                if vagas in [0, 1]:
                    return vagas

                print("Digite 0 ou 1.")

            except ValueError:
                print("Digite um número válido.")

    while True:
        try:
            vagas = int(input(
                "Quantas vagas adicionais deseja além do pacote inicial de 2? "
            ))

            if vagas >= 0:
                return vagas

            print("A quantidade não pode ser negativa.")

        except ValueError:
            print("Digite um número válido.")


def solicitar_criancas(tipo):
    if tipo != "Apartamento":
        return True

    while True:
        resposta = input(
            "Existem crianças no imóvel? (1 = Sim / 0 = Não): "
        )

        if resposta == "1":
            return True
        elif resposta == "0":
            return False

        print("Digite apenas 1 ou 0.")


def solicitar_parcelas():
    while True:
        try:
            parcelas = int(input(
                "Em quantas vezes deseja parcelar a taxa contratual? (1 a 5): "
            ))

            if parcelas in [1, 2, 3, 4, 5]:
                return parcelas

            print("Escolha entre 1 e 5 parcelas.")

        except ValueError:
            print("Digite um número válido.")


def main():
    print("===== RENTSMART - ORÇAMENTO DE LOCAÇÃO =====")

    tipo = solicitar_tipo_imovel()
    quartos = solicitar_quartos(tipo)
    vagas = solicitar_vagas(tipo)
    tem_criancas = solicitar_criancas(tipo)
    parcelas = solicitar_parcelas()

    imovel = Imovel(tipo, quartos, vagas)
    orcamento = Orcamento(imovel, tem_criancas, parcelas)

    print("\n===== RESUMO DO ORÇAMENTO =====")
    print("Tipo de imóvel:", tipo)
    print("Quartos:", quartos)
    print("Vagas:", vagas)

    if tipo == "Apartamento":
        print("Existem crianças:", "Sim" if tem_criancas else "Não")
    else:
        print("Existem crianças: Não se aplica")

    print("Aluguel base: R$ {:.2f}".format(
        imovel.calcular_aluguel_base()
    ))
    print("Adicional de quartos: R$ {:.2f}".format(
        imovel.calcular_adicional_quartos()
    ))
    print("Adicional de garagem: R$ {:.2f}".format(
        imovel.calcular_adicional_garagem()
    ))
    print("Desconto: R$ {:.2f}".format(
        orcamento.calcular_desconto()
    ))
    print("Aluguel mensal final: R$ {:.2f}".format(
        orcamento.calcular_aluguel_final()
    ))
    print("Taxa contratual: R$ {:.2f}".format(
        orcamento.taxa_contratual
    ))
    print("Quantidade de parcelas:", parcelas)
    print("Valor de cada parcela: R$ {:.2f}".format(
        orcamento.calcular_parcela_contratual()
    ))

    gerador = GeradorCSV(orcamento)
    gerador.gerar_arquivo()


if __name__ == "__main__":
    main()
