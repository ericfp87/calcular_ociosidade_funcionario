import pandas as pd

# Carregar o arquivo .parquet
df = pd.read_parquet('seu_arquivo.parquet')

# Converter a coluna DataHoraServico para o tipo datetime
df['DataHoraServico'] = pd.to_datetime(df['DataHoraServico'])

# Extrair a data (sem a hora) para um novo coluna
df['Data'] = df['DataHoraServico'].dt.date

# Função para calcular a maior diferença de horários em um dia
def calcular_maior_diferenca(grupo):
    if len(grupo) < 2:
        return pd.Timedelta(0)
    diferencas = grupo['DataHoraServico'].diff().dropna()
    return diferencas.max()

# Agrupar por Nome e Data e aplicar a função
result = df.groupby(['Nome', 'Data']).apply(calcular_maior_diferenca).reset_index(name='MaiorDiferenca')

# Salvar o resultado em um arquivo CSV
result.to_csv('resultado_ociosidade.csv', index=False)

print("Arquivo CSV criado com sucesso.")
