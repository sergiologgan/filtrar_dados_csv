import csv
import logging

# Configuração de logging para registrar erros
logging.basicConfig(filename='error_log.txt', level=logging.ERROR, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

def filtrar_valores_transacoes(arquivo_entrada, arquivo_saida, valor_minimo):
    """
    Esta função serve para filtrar valores do arquivo "transacoes.csv" verificando
    pela coluna "Valor da transação" se é maior que 1000. Se caso for, gerar e inserir o valor no arquivo
    "transacoes_altas.csv"
    """
    try:
        # Ler o arquivo CSV
        with open(arquivo_entrada, mode='r', newline='', encoding='utf-8') as file:
            leitor = csv.reader(file)
            cabecalho = next(leitor)  # Ler o cabeçalho, ou seja obtem o proximo item do iterador
            transacoes_altas = [cabecalho]  # Listar para armazenar transações altas

            # Filtrar as transações
            for linha in leitor:
                try:
                    # Converter o valor da transação para float e verificar se é maior que o valor mínimo
                    if float(linha[1]) > valor_minimo:
                        transacoes_altas.append(linha)
                except ValueError as e:
                    # Registrar um erro caso não consiga converter o valor para float
                    logging.error(f'Erro ao processar linha {linha}: {e}')

        # Salvar as transações filtradas em um novo arquivo CSV
        with open(arquivo_saida, mode='w', newline='', encoding='utf-8') as file:
            escritor = csv.writer(file)
            escritor.writerows(transacoes_altas)

    except Exception as e:
        # Registrar um erro genérico se algo inesperado acontecer
        logging.error(f'Erro ao acessar o arquivo {arquivo_entrada}: {e}')


#-------------------<Entradas e Saídas>
caminhoEntradaCSV = r'C:\Users\sserg\OneDrive\Área de Trabalho\Delfia\Processamento de dados\transacoes.csv'
caminhoSaidaCSV = r'C:\Users\sserg\OneDrive\Área de Trabalho\Delfia\Processamento de dados\transacoes_altas.csv'

"""
arquivo_entrada -> CSV de entrada
arquivo_saida -> CSV de saída
valor_minimo -> filtrar as transações maiores ou iguais ao número inserido
"""
filtrar_valores_transacoes(caminhoEntradaCSV, caminhoSaidaCSV, 1000)
