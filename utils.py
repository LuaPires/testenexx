import logging
from datetime import datetime

class Service:

    def formatar_data(data):
        try:
            return datetime.strptime(data, '%d/%m/%y').strftime('%d/%B/%Y')
        except ValueError as e:
            logging.error(f"Erro ao formatar data: {e}")
            return data

    def remover_formatacao_numero_inscricao(num_inscricao):
        return ''.join(filter(str.isdigit, str(num_inscricao)))

    def formatar_valor(valor):
        try:
            return f"{float(valor):,.2f}".replace('.', ',')
        except ValueError as e:
            logging.error(f"Erro ao formatar valor: {e}")
            return valor