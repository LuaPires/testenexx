# Processador de Arquivo Excel para CSV

Este projeto é uma aplicação Python que processa arquivos no formato `.xlsx` e gera relatórios formatados em CSV. Ele suporta diferentes arquivos de entrada desde que sigam a mesma estrutura especificada e pode ser executado via linha de comando.

## Estrutura do Projeto

- `app.py`: Script principal que realiza a leitura, processamento e geração do arquivo CSV.
- `arquivo_entrada.xlsx`: Arquivo de entrada que será processado (não incluído no repositório; deve ser fornecido no momento da execução).
- `saida_csv.csv`: Arquivo de saída gerado pelo script contendo o relatório final em formato CSV.

## Requisitos

Antes de executar a aplicação, certifique-se de que os seguintes pacotes estão instalados:

- Python 3.6 + 
- Pandas

### Instalação de Dependências

1. Crie e ative um ambiente virtual (opcional, mas recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux
   ```

2. Instale a biblioteca necessária:

   ```bash
   pip install -r requirements.txt
   ```

## Execução

A aplicação deve ser executada via linha de comando, passando o arquivo de entrada `.xlsx` e o arquivo de saída `.csv` como argumentos.

### Comando de Execução:

```bash
python app.py arquivo_entrada.xlsx saida_csv.csv
```

- `arquivo_entrada.xlsx`: Caminho para o arquivo Excel de entrada que será processado.
- `saida_csv.csv`: Caminho onde o arquivo CSV será gerado.

### Exemplo:

```bash
python app.py ./dados/arquivo_entrada.xlsx ./relatorios/saida_csv.csv
```

### Logs:

Durante o processamento, o sistema gera logs das etapas, que são exibidos diretamente no console. Isso inclui:
- Leitura do arquivo de entrada
- Aplicação das transformações de dados
- Geração do arquivo CSV

## Formatação e Regras de Processamento

### Tradução de Colunas

As colunas do arquivo de saída (CSV) são geradas conforme as seguintes regras de mapeamento:

| CSV Saída             | XLSX Entrada         |
|-----------------------|----------------------|
| Nome Empresa          | Coluna A             |
| Numero Incricao Empresa | Coluna B (sem formatação) |
| Nome Banco            | Coluna C             |
| Nome da Rua           | Coluna D             |
| Numero do Local       | Coluna E             |
| Cidade                | Coluna F             |
| Estado                | Coluna G (sigla -> nome) |
| Forma Lancamento      | Coluna H             |
| Nome Favorecido       | Coluna I             |
| Data Pagamento        | Coluna J (formato dd/mes/ano) |
| Valor Pagamento       | Coluna K (formatação com vírgulas) |
| Numero Documento      | Coluna L             |

### Regras Adicionais

- **Remoção de Formatação**: O número de inscrição na Coluna B do Excel deve ter toda a formatação (pontos e barras) removida.
- **Tradução de Estados**: As siglas dos estados na Coluna G são convertidas para seus nomes completos.
- **Formatação de Datas**: Datas na Coluna J são convertidas para o formato `dd/mes por extenso/ano`.
- **Formatação de Valores**: Valores na Coluna K são formatados com vírgulas, por exemplo, `1,200.50` torna-se `1.200,50`.
- **Ordenação por Prioridade**: Os registros são ordenados pela Coluna H, em ordem crescente."# testenxx" 
