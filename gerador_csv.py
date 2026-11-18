
import csv
import os

class GeradorCSV:
    def __init__(self, orcamento):
        self.orcamento = orcamento

    def gerar_arquivo(self):
        pasta = os.path.dirname(os.path.abspath(__file__))
        nome_arquivo = os.path.join(pasta, "orcamento_12_meses.csv")

        valor_parcela = self.orcamento.calcular_parcela_contratual()
        saldo_taxa = self.orcamento.taxa_contratual

        with open(nome_arquivo, "w", newline="", encoding="utf-8-sig") as arquivo:
            escritor = csv.writer(arquivo, delimiter=";")

            escritor.writerow([
                "Mês",
                "Aluguel mensal",
                "Parcela da taxa contratual",
                "Total do mês",
                "Saldo da taxa contratual"
            ])

            for mes in range(1, 13):
                if mes <= self.orcamento.parcelas:
                    parcela = valor_parcela
                    saldo_taxa = max(0, saldo_taxa - parcela)
                else:
                    parcela = 0

                aluguel = self.orcamento.calcular_aluguel_final()
                total = aluguel + parcela

                escritor.writerow([
                    mes,
                    f"{aluguel:.2f}",
                    f"{parcela:.2f}",
                    f"{total:.2f}",
                    f"{saldo_taxa:.2f}"
                ])

        print("Arquivo CSV gerado:", nome_arquivo)
