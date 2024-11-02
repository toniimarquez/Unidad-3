import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

mu = 10.0 
sigma = 2.0 
n = 50  

U = np.random.uniform(0, 1, n)
Z = mu + sigma * stats.norm.ppf(U)
T = np.exp(Z) 

print("Tiempos de inactividad generados:", T)

plt.hist(T, bins=20, edgecolor='black', density=True)

x = np.linspace(min(T), max(T), 100)
pdf = stats.lognorm.pdf(x, sigma, scale=np.exp(mu))
plt.plot(x, pdf, 'r', label='Distribución lognormal teórica')

plt.title("Histograma de los tiempos de inactividad (Distribución Lognormal)")
plt.xlabel("Tiempo de inactividad")
plt.ylabel("Densidad de probabilidad")
plt.legend()
plt.show()
