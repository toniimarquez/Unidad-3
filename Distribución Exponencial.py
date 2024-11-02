import numpy as np
import matplotlib.pyplot as plt

tiempo_promedio_servicio = 15
lambda_servicio = 1 / tiempo_promedio_servicio
horas_trabajo = 12
minutos_totales = horas_trabajo * 60

n_servicios_esperados = int(minutos_totales / tiempo_promedio_servicio)

def generar_tiempo_servicio(lambda_servicio):
    u = np.random.uniform(0, 1)
    tiempo_servicio = -1 / lambda_servicio * np.log(1 - u)
    return tiempo_servicio

tiempos_servicio = [generar_tiempo_servicio(lambda_servicio) for _ in range(n_servicios_esperados)]

tiempo_total = sum(tiempos_servicio)
tiempo_promedio_real = np.mean(tiempos_servicio)
numero_servicios = len(tiempos_servicio)

print(f"Estadísticas de la simulación:")
print(f"Número de servicios en 12 horas: {numero_servicios}")
print(f"Tiempo promedio de servicio real: {tiempo_promedio_real:.2f} minutos")
print(f"Tiempo total acumulado: {tiempo_total:.2f} minutos ({tiempo_total/60:.2f} horas)")

plt.figure(figsize=(10, 6))
plt.hist(tiempos_servicio, bins=20, edgecolor='black', alpha=0.7)
plt.title(f'Distribución de Tiempos de Servicio en 12 horas\n(Tiempo promedio objetivo: {tiempo_promedio_servicio} min)')
plt.xlabel('Tiempo de servicio (minutos)')
plt.ylabel('Frecuencia')

plt.show()
