# pip install dash
# pip install pandas
# pip install openpyxl

# layout -> tudo que vai ser visualizado
# callbacks -> funcionalidades que teremos no dash

from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px
import  plotly.figure_factory as ff


app = Dash(__name__)

df = pd.read_excel('numero_atendentes_necessarios_NAN.xlsx')
# esta linha lê o arquivo excel e aramazena os dados em uma variável chamada df -> data frame
cores  =  [ 'slategray' ,  'magenta']


fig  =  px.line (df,  x = "Hora Fim (x)" ,  y = "Número Médio Ligantes f(x)")
                         

opcoes = list(df['Momento'].unique())
# esta linha cria uma lista contendo  os valores únicos da coluna 'Momentos'

opcoes.append('Todos os Momentos')
# esta linha adiciona a string 'Todos os Momentos' ao final da lista opcoes

app.layout = html.Div(children=[
    html.H1(children='Número de Ligantes'),
    html.H2(children='Gráfico f(x) do número médio de ligantes separados em momentos identificadores de 1 até N, N=96'),
    dcc.Dropdown(opcoes, value='Todos os Momentos', id='lista_momentos'),

    dcc.Graph(
        id = 'grafico_ligacoes_momentos',
        figure = fig
    )
])

@app.callback(
    Output('grafico_ligacoes_momentos', 'figure'),
    Input('lista_momentos', 'value')
)

def update_output(value):
    if value == 'Todos os Momentos':
        fig  =  px.line (df,  x = "Hora Fim (x)" ,  y = "Número Médio Ligantes f(x)")
    else:
        tabela_filtrada = df.loc[df['Momento'] == value, :]
        fig  =  px.line (df,  x = "Hora Fim (x)" ,  y = "Número Médio Ligantes f(x)" )

    return fig

if __name__ == '__main__':
    app.run(debug=True)