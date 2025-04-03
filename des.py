import matplotlib.pyplot as plt


# Criar uma figura e um eixo
fig, ax = plt.subplots()

# Desenhar um círculo
circle = plt.Circle((0.5, 0.5), 0.5, color='blue')
ax.add_artist(circle)

# Configurações do eixo
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Mostrar o desenho
plt.show()
