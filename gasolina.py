import pandas as pd
import matplotlib.pyplot as plt

# Carregando dados do arquivo CSV
df = pd.read_csv('gasolina.csv')

# Criando gráfico de linha
plt.figure(figsize=(10, 6))
plt.plot(df['dia'], df['venda'], marker='o', linestyle='-', color='b')

# Adicionando rótulos e título
plt.title('Preço da Gasolina ao Longo dos Dias')
plt.xlabel('Dia')
plt.ylabel('Preço (R$)')

# Salvando o gráfico em um arquivo PNG
plt.savefig('gasolina.png')

# Exibindo o gráfico
plt.show()
