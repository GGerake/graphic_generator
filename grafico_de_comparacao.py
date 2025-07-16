import matplotlib.pyplot as plt
import numpy as np

# Critérios
categories = [
    "Escalabilidade",
    "Performance",
    "Comunidade/Documentação",
    "Complexidade (quanto menor, melhor)",
    "Posicionamento no mercado",
    "Compatibilidade com outros sistemas"
]

# Pontuações (0 a 10)
# Nota: Complexidade é invertida (quanto menor, melhor), então será ajustada no gráfico
scores = {
    "Node.js + TS": [8, 7, 10, 6, 9, 9],
    "C# + .NET":    [9, 8, 9, 5, 10, 8],
    "Go":           [9, 10, 8, 9, 7, 9]
}

# Inverter pontuação de complexidade (quanto menor, melhor)
complexity_index = categories.index("Complexidade (quanto menor, melhor)")
for lang in scores:
    scores[lang][complexity_index] = 10 - scores[lang][complexity_index] + 1

# Criar gráfico radar
labels = np.array(categories)
num_vars = len(categories)

angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

for lang, values in scores.items():
    values += values[:1]  # fechar o gráfico
    ax.plot(angles, values, label=lang)
    ax.fill(angles, values, alpha=0.1)

ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)
ax.set_thetagrids(np.degrees(angles[:-1]), labels)
ax.set_ylim(0, 10)
ax.set_title("Comparativo Backend: Node.js + TS vs C# .NET vs Go", size=14)
ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.2), ncol=1)

plt.tight_layout()
plt.show()
