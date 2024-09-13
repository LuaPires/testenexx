import pandas as pd
import sys
import logging
from utils import Service

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

ESTADOS = {
    'AC': 'Acre',
    'AL': 'Alagoas',
    'AP': 'Amapá',
    'AM': 'Amazonas',
    'BA': 'Bahia',
    'CE': 'Ceará',
    'DF': 'Distrito Federal',
    'ES': 'Espírito Santo',
    'GO': 'Goiás',
    'MA': 'Maranhão',
    'MT': 'Mato Grosso',
    'MS': 'Mato Grosso do Sul',
    'MG': 'Minas Gerais',
    'PA': 'Pará',
    'PB': 'Paraíba',
    'PR': 'Paraná',
    'PE': 'Pernambuco',
    'PI': 'Piauí',
    'RJ': 'Rio de Janeiro',
    'RN': 'Rio Grande do Norte',
    'RS': 'Rio Grande do Sul',
    'RO': 'Rondônia',
    'RR': 'Roraima',
    'SC': 'Santa Catarina',
    'SP': 'São Paulo',
    'SE': 'Sergipe',
    'TO': 'Tocantins'
}


def processar_arquivo(entrada, saida):
    try:
        logging.info(f"Lendo arquivo de entrada: {entrada}")
        df = pd.read_excel(entrada)

        df.columns = [
            "Nome Empresa", "Numero Incricao Empresa", "Nome Banco", "Nome da Rua", "Numero do Local",
            "Cidade", "Estado", "Forma Lancamento", "Nome Favorecido", "Data Pagamento",
            "Valor Pagamento", "Numero Documento"
        ]

        logging.info("Aplicando transformações nos dados...")

        df['Numero Incricao Empresa'] = df['Numero Incricao Empresa'].apply(Service.remover_formatacao_numero_inscricao)

        df['Estado'] = df['Estado'].map(ESTADOS)

        df['Data Pagamento'] = df['Data Pagamento'].apply(Service.formatar_data)

        df['Valor Pagamento'] = df['Valor Pagamento'].apply(Service.formatar_valor)

        df = df.sort_values(by='Forma Lancamento')

        logging.info(f"Gerando arquivo CSV de saída: {saida}")
        df.to_csv(saida, index=False, sep=';', encoding='utf-8')

        logging.info("Processamento concluído com sucesso.")

    except Exception as e:
        logging.error(f"Erro durante o processamento: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso correto: python app.py arquivo_entrada.xlsx saida_csv.csv")
    else:
        arquivo_entrada = sys.argv[1]
        arquivo_saida = sys.argv[2]
        processar_arquivo(arquivo_entrada, arquivo_saida)
