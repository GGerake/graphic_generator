import json
import plotly.graph_objects as go

# Ler dados do JSON
with open('dados_gerais.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

categories = data["categorias"]
scores = data["pontuacoes"]

# Fechar o gráfico (repetir o primeiro valor no final)
categories += [categories[0]]

fig = go.Figure()

# Adicionar cada linguagem como uma linha no radar
for lang, values in scores.items():
    values += [values[0]]  # fecha o gráfico
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name=lang
    ))

# Configurar layout
fig.update_layout(
    polar=dict(
        radialaxis=dict(visible=True, range=[0, 10])
    ),
    showlegend=True,
    title="Comparativo Backend: Node.js + TS vs C# .NET vs Go"
)

fig.show()
