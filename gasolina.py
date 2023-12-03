import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregando os dados do arquivo gasolina.csv
df = pd.read_csv('gasolina.csv')

# Configurando o estilo do Seaborn (opcional)
sns.set(style="whitegrid")

# Criando o gráfico de linha
plt.figure(figsize=(10, 6))
sns.lineplot(x='dia', y='venda', data=df, marker='o', color='blue')

# Adicionando rótulos e título
plt.xlabel('Dia')
plt.ylabel('Preço de Venda (R$)')  # Modificado para refletir a unidade monetária
plt.title('Variação do Preço de Venda de Gasolina ao Longo dos Dias')

# Adicionando uma legenda (opcional)
plt.legend(['Preço de Venda'])

# Salvando o gráfico como um arquivo PNG
plt.savefig('gasolina.png')

# Mostrando o gráfico (opcional)
plt.show()

#  Salvando o código Python em um arquivo
code = """
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregando os dados do arquivo gasolina.csv
df = pd.read_csv('gasolina.csv')

# Configurando o estilo do Seaborn (opcional)
sns.set(style="whitegrid")

# Criando o gráfico de linha
plt.figure(figsize=(10, 6))
sns.lineplot(x='dia', y='venda', data=df, marker='o', color='blue')

# Adicionando rótulos e título
plt.xlabel('Dia')
plt.ylabel('Preço de Venda (R$)')  # Modificado para refletir a unidade monetária
plt.title('Variação do Preço de Venda de Gasolina ao Longo dos Dias')

# Adicionando uma legenda (opcional)
plt.legend(['Preço de Venda'])

# Salvando o gráfico como um arquivo PNG
plt.savefig('gasolina.png')

# Mostrando o gráfico (opcional)
plt.show()
"""

with open('gasolina.py', 'w') as file:
    file.write(code)
