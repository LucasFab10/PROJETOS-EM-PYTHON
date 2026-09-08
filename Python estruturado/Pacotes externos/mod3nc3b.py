# Gerar 1000 pontos seguindo a distribuição normal
# com media 20 e desvio padrão 2
# exibir em um histograma
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1)
dados = np.random.normal(loc=20, scale=2, size=1000)
print(dados)
plt.hist(dados, color = 'lightblue', ec = 'red')
plt.show()