import matplotlib.pyplot as plt

resistores = [100, 470, 1000, 4700, 10000, 33000]
tempo_carga_1 = [1.505, 3.358, 5.141, 14.555, 20.577, 30.707]
tempo_descarga_1 = [1, 4.7, 10, 47, 100, 330]
Vmax = [8.99, 8.99, 8.84, 8.59, 7.85, 5.45]

capacitores = [10e-9, 100e-9, 470e-9, 100e-6, 420e-6, 1000e-6]
tempo_carga_2 = [0.05, 0.5, 2.35, 50, 210, 500]
tempo_descarga_2 = [0.05, 0.5, 2.35, 50, 210, 500]

# Gráfico de carga 1
plt.figure(figsize=(10, 6))
plt.plot(tempo_carga_1, Vmax, label='Tempo de Carga')
plt.ylabel('VMax (V)')
plt.xlabel('Tempo (ms)')
plt.title('Resistência para Diferentes Tempos de Carga')
plt.legend()
plt.show()

# Gráfico de descarga 1
plt.figure(figsize=(10, 6))
plt.plot(tempo_descarga_1, Vmax, label='Tempo de Descarga')
plt.ylabel('Resistência (Ohms)')
plt.xlabel('Tempo (ms)')
plt.title('Resistência para Diferentes Tempos de Descarga')
plt.legend()
plt.show()

# Gráfico de carga 2
plt.figure(figsize=(10, 6))
plt.plot(tempo_carga_2, capacitores, label='Tempo de Carga')
plt.ylabel('Capacitância (Farads)')
plt.xlabel('Tempo (ms)')
plt.title('Capacitância para Diferentes Tempos de Carga')
plt.legend()
plt.show()

# Gráfico de descarga 2
plt.figure(figsize=(10, 6))
plt.plot(tempo_descarga_2, capacitores, label='Tempo de Descarga')
plt.ylabel('Capacitância (Farads)')
plt.xlabel('Tempo (ms)')
plt.title('Tempo de Descarga para Diferentes Capacitores')
plt.legend()
plt.show()