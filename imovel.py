
class Imovel:
    def __init__(self, tipo, quartos, vagas=0):
        tipos_validos = ["Apartamento", "Casa", "Estúdio"]

        if tipo not in tipos_validos:
            raise ValueError("Tipo de imóvel inválido.")

        if tipo in ["Apartamento", "Casa"] and quartos not in [1, 2]:
            raise ValueError("Escolha 1 ou 2 quartos.")

        if tipo == "Estúdio" and quartos != 0:
            raise ValueError("Estúdio não possui quartos separados.")

        if vagas < 0:
            raise ValueError("A quantidade de vagas não pode ser negativa.")

        if tipo in ["Apartamento", "Casa"] and vagas not in [0, 1]:
            raise ValueError("Escolha 0 ou 1 vaga.")

        self.tipo = tipo
        self.quartos = quartos
        self.vagas = vagas

    def calcular_aluguel_base(self):
        valores = {
            "Apartamento": 700,
            "Casa": 900,
            "Estúdio": 1200
        }
        return valores[self.tipo]

    def calcular_adicional_quartos(self):
        if self.tipo == "Apartamento" and self.quartos == 2:
            return 200
        elif self.tipo == "Casa" and self.quartos == 2:
            return 250
        return 0

    def calcular_adicional_garagem(self):
        if self.tipo in ["Apartamento", "Casa"]:
            return 300 if self.vagas == 1 else 0
        elif self.tipo == "Estúdio":
            return 250 + (self.vagas * 60)
        return 0

    def calcular_desconto(self, tem_criancas):
        if self.tipo == "Apartamento" and not tem_criancas:
            subtotal = (
                self.calcular_aluguel_base()
                + self.calcular_adicional_quartos()
                + self.calcular_adicional_garagem()
            )
            return subtotal * 0.05
        return 0

