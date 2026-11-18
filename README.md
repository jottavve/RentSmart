
# RentSmart - Sistema de Orçamento de Locação

## Sobre o projeto

O RentSmart é um sistema desenvolvido em Python para automatizar a elaboração de orçamentos de locação de imóveis da imobiliária R.M Imóveis.

O programa recebe as características do imóvel, calcula o valor do aluguel, aplica adicionais e descontos, calcula a taxa contratual e gera um arquivo CSV com a projeção financeira de 12 meses.

## Funcionalidades

- Cadastro do tipo de imóvel.
- Seleção da quantidade de quartos.
- Seleção de vagas de garagem.
- Aplicação de adicionais e descontos.
- Cálculo do aluguel mensal.
- Parcelamento da taxa contratual em até 5 vezes.
- Geração de arquivo CSV com projeção de 12 meses.
- Validação das informações fornecidas pelo usuário.

## Regras de negócio

| Tipo de imóvel | Valor base |
|---|---:|
| Apartamento com 1 quarto | R$ 700,00 |
| Casa com 1 quarto | R$ 900,00 |
| Estúdio | R$ 1.200,00 |

### Adicionais

- Apartamento com 2 quartos: R$ 200,00.
- Casa com 2 quartos: R$ 250,00.
- Apartamento ou casa com vaga: R$ 300,00.
- Estúdio: pacote inicial de 2 vagas por R$ 250,00.
- Cada vaga adicional no estúdio: R$ 60,00.

### Desconto

Apartamentos sem crianças recebem desconto de 5% sobre o valor do aluguel após os adicionais.

### Taxa contratual

A taxa contratual é de R$ 2.000,00 e pode ser parcelada em até 5 vezes. Ela é apresentada separadamente do aluguel mensal.

## Estrutura do projeto

- `main.py`: execução principal e entrada de dados.
- `imovel.py`: classe responsável pelas características e cálculos do imóvel.
- `orcamento.py`: classe responsável pelos cálculos do orçamento.
- `gerador_csv.py`: classe responsável pela geração da projeção financeira.
- `orcamento_12_meses.csv`: arquivo gerado com a projeção dos 12 meses.

## Tecnologias utilizadas

- Python 3
- Programação Orientada a Objetos (POO)
- Biblioteca csv
- Biblioteca os

## Como executar

1. Tenha o Python 3 instalado.
2. Deixe todos os arquivos do projeto na mesma pasta.
3. Abra o terminal nessa pasta.
4. Execute o comando:

```bash
python main.py
```

5. Informe os dados solicitados pelo programa.
6. Consulte o arquivo `orcamento_12_meses.csv` gerado na pasta do projeto.

## Programação Orientada a Objetos

O projeto utiliza classes, objetos, atributos, métodos e encapsulamento da lógica de cada responsabilidade.

As classes `Imovel`, `Orcamento` e `GeradorCSV` dividem as funcionalidades do sistema, facilitando a organização e a manutenção do código.

## Desenvolvido para fins acadêmicos

Projeto acadêmico da disciplina de programação.
