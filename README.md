# Filtro de Transações Altas

## Descrição
Este script Python filtra e salva transações acima de um determinado valor mínimo de um arquivo CSV de entrada para um arquivo CSV de saída. O script também registra erros durante a execução, salvando detalhes no arquivo `error_log.txt`.

## Pré-requisitos
Para executar este script, você precisará de:
- Python 3.x instalado em sua máquina.

## Configuração
1. Clone o repositório para sua máquina local usando:
   ```python
   git clone https://github.com/sergiologgan/filtrar_dados_csv.git
   ```
2. Navegue até o diretório do projeto.

## Uso
Antes de executar o script, certifique-se de que o caminho para os arquivos CSV de entrada e saída estão corretamente definidos nas variáveis `caminhoEntradaCSV` e `caminhoSaidaCSV`.

Execute o script com o seguinte comando:
```python
python filtrar_transacoes.py
```

## Funcionamento
O script faz o seguinte:
- Abre o arquivo CSV de entrada.
- Lê cada linha e verifica se o valor da transação é maior que o valor mínimo especificado (neste caso, 1000).
- Salva as transações que atendem ao critério em um novo arquivo CSV.
- Registra erros relacionados à leitura e processamento de dados no arquivo `error_log.txt`.

## Licença
MIT
