
class Orcamento:
    def __init__(self, imovel, tem_criancas, parcelas):
        if parcelas not in [1, 2, 3, 4, 5]:
            raise ValueError("Escolha entre 1 e 5 parcelas.")

        self.imovel = imovel
        self.tem_criancas = tem_criancas
        self.parcelas = parcelas
        self.taxa_contratual = 2000

    def calcular_subtotal(self):
        return (
            self.imovel.calcular_aluguel_base()
            + self.imovel.calcular_adicional_quartos()
            + self.imovel.calcular_adicional_garagem()
        )

    def calcular_desconto(self):
        return self.imovel.calcular_desconto(self.tem_criancas)

    def calcular_aluguel_final(self):
        return self.calcular_subtotal() - self.calcular_desconto()

    def calcular_parcela_contratual(self):
        return self.taxa_contratual / self.parcelas
