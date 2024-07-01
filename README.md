## Descrição do Projeto

Este projeto utiliza a biblioteca Pandas do Python para processar e analisar dados de um arquivo `.parquet`. O objetivo principal é calcular a maior diferença de horários em um dia para cada nome, agrupando os dados por nome e data, e salvar o resultado em um arquivo CSV.

## Funcionamento do Código

### Importação da Biblioteca

```python
import pandas as pd
```

O código começa importando a biblioteca `pandas`, que é usada para manipulação e análise de dados.

### Carregamento do Arquivo `.parquet`

```python
df = pd.read_parquet('seu_arquivo.parquet')
```

O arquivo `.parquet` é carregado em um DataFrame do Pandas. Certifique-se de substituir `'seu_arquivo.parquet'` pelo caminho correto do seu arquivo.

### Conversão de Coluna para Tipo Datetime

```python
df['DataHoraServico'] = pd.to_datetime(df['DataHoraServico'])
```

A coluna `DataHoraServico` é convertida para o tipo `datetime`, permitindo operações de data e hora.

### Extração da Data

```python
df['Data'] = df['DataHoraServico'].dt.date
```

Uma nova coluna `Data` é criada, extraindo apenas a data (sem a hora) da coluna `DataHoraServico`.

### Função para Calcular a Maior Diferença de Horários em um Dia

```python
def calcular_maior_diferenca(grupo):
    if len(grupo) < 2:
        return pd.Timedelta(0)
    diferencas = grupo['DataHoraServico'].diff().dropna()
    return diferencas.max()
```

A função `calcular_maior_diferenca` calcula a maior diferença de horários em um dia para um grupo específico. Se houver menos de dois registros no grupo, a diferença é zero. Caso contrário, as diferenças entre os horários são calculadas e a maior diferença é retornada.

### Agrupamento e Aplicação da Função

```python
result = df.groupby(['Nome', 'Data']).apply(calcular_maior_diferenca).reset_index(name='MaiorDiferenca')
```

Os dados são agrupados por `Nome` e `Data`, e a função `calcular_maior_diferenca` é aplicada a cada grupo. O resultado é um DataFrame com a maior diferença de horários para cada nome em cada dia.

### Salvamento do Resultado em um Arquivo CSV

```python
result.to_csv('resultado_ociosidade.csv', index=False)
```

O resultado é salvo em um arquivo CSV chamado `resultado_ociosidade.csv`. O parâmetro `index=False` garante que os índices não sejam incluídos no arquivo.

### Mensagem de Conclusão

```python
print("Arquivo CSV criado com sucesso.")
```

Uma mensagem é exibida no console indicando que o arquivo CSV foi criado com sucesso.

## Como Executar

1. Certifique-se de ter o arquivo `.parquet` com os dados necessários.
2. Atualize o caminho do arquivo `.parquet` no código, se necessário.
3. Execute o script em um ambiente Python com a biblioteca Pandas instalada.
4. Verifique o arquivo `resultado_ociosidade.csv` gerado na mesma pasta do script.

## Requisitos

- Python 3.x
- Pandas

```sh
pip install pandas
```

 
