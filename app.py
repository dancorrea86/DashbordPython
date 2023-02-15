from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import  plotly.express as px
import pandas as pd

dataframe = pd.read_csv("arquivo_csv/dados.csv", sep=";")
print(dataframe)


app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

grafico = dcc.Graph(
    id='meu_grafico',
)

dropdown = dcc.Dropdown(
    [
        {
            "label": html.Span(['jan/22'], style={'color': 'Gold', 'font-size': 20}),
            "value": "jan/22",
        },
        {
            "label": html.Span(['fev/22'], style={'color': 'Gold', 'font-size': 20}),
            "value": "fev/22",
        },
        {
            "label": html.Span(['mar/22'], style={'color': 'Gold', 'font-size': 20}),
            "value": "mar/22",
        },
        {
            "label": html.Span(['abril/22'], style={'color': 'Gold', 'font-size': 20}),
            "value": "abr/22",
        },
        {
            "label": html.Span(['mai/22'], style={'color': 'Gold', 'font-size': 20}),
            "value": "mai/22",
        },
        {
            "label": html.Span(['jun/22'], style={'color': 'Gold', 'font-size': 20}),
            "value": "jun/22",
        },
        {
            "label": html.Span(['jul/22'], style={'color': 'Gold', 'font-size': 20}),
            "value": "jul/22",
        },
        {
            "label": html.Span(['ago/22'], style={'color': 'Gold', 'font-size': 20}),
            "value": "ago/22",
        },
                {
            "label": html.Span(['set/22'], style={'color': 'Gold', 'font-size': 20}),
            "value": "set/22",
        },
        {
            "label": html.Span(['out/22'], style={'color': 'Gold', 'font-size': 20}),
            "value": "out/22'",
        },
        {
            "label": html.Span(['nov/22'], style={'color': 'Gold', 'font-size': 20}),
            "value": "nov/22'",
        },
        {
            "label": html.Span(['dez/22'], style={'color': 'Gold', 'font-size': 20}),
            "value": "dez/22",
        },
        {
            "label": html.Span(['jan/23'], style={'color': 'Gold', 'font-size': 20}),
            "value": "jan/23",
        },
        {
            "label": html.Span(['fev/23'], style={'color': 'Gold', 'font-size': 20}),
            "value": "fev/23",
        },
    ], value='jan/22',
    id='meu_dropdown'
)

app.layout = html.Div(
    children=[
        html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col(html.H1("Dashboard Gastos")),
                        dbc.Col(dropdown),
                    ]
                ),
                dbc.Row(
                    [
                        html.Div(grafico),
                    ]
                ),
            ]
        )
    ]
)


@app.callback(
    Output('meu_grafico', 'figure'),
    [
        Input('meu_dropdown', 'value')
    ]
)

def my_callback(input_data):
    filtered_dataframe = dataframe.loc[dataframe['Competencia'] == input_data]
    fig = px.bar(filtered_dataframe, x='Categoria',y='Valor')
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)