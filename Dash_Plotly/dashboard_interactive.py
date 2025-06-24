import pandas as pd
import numpy as np
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
import dash, logging
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
pio.renderers.default ='browser'
logging.basicConfig(level=logging.INFO)
data = pd.read_csv('../Dash_Plotly/global_cancer_patients_2015_2024.csv')
print(f'data: {data.head(5)}')

## tablea de board avec dash

app = Dash(__name__)

app.layout = html.Div(children=
                      [
        html.H1("Vue Global des Personnes Atteintes de Cancer (2015-2024)",style={"textAlign":'center', "font-size":24}),
        html.Div(["Input Year: ",
                  dcc.Input(id='input-year',
                            type='number',
                            value='2015',
                            style={
                                "height":30, 
                                "width":100,
                                }
                                ),],
                                style={"textAlign":'center', "font-size":20}),
        html.Br(),
        html.Br(),
        dcc.Graph(id="line-plot"),
        html.Br(),
        dcc.Graph(id="bar-plot"),

    ]
)

@app.callback(
    Output(component_id='line-plot', component_property='figure'),
    Output('bar-plot', 'figure'),
    Input(component_id='input-year', component_property='value')
    )

def update_year(year_entered):

    data_year = data[data['Year']==int(year_entered)]
    genetic_risk = data_year.groupby('Genetic_Risk')["Target_Severity_Score"].mean().reset_index()
    age_moy_gender = data_year.groupby('Gender')['Age'].mean().reset_index()
    fig1 = go.Figure(data=go.Line(
        x=genetic_risk['Genetic_Risk'],
        y=genetic_risk['Target_Severity_Score'],
        mode='lines+markers',
        marker=dict(color='green', size=10),
        line=dict(color='blue', width=2)
    )
    )

    fig2 =go.Figure(data = go.Bar(
        x=age_moy_gender['Gender'],
        y=age_moy_gender['Age'],
        marker_color="indigo"
    ))

    fig2.update_layout(title="Evolution de l'age en fonction du sexe",
                       xaxis_title="Gender",
                       yaxis_title="Age")
    fig1.update_layout(title="Evolution du Score de Gravité Ciblé en Fonction du Risque Génétiques",
                      xaxis_title="Risque Génétiques",
                      yaxis_title="Score de Gravité Ciblé",
                      template="plotly_dark",
                      width=800,
                      height=600,
                      margin=dict(l=50, r=50, t=50, b=50)
                      )
    return fig1, fig2


if __name__=="__main__":
    app.run(debug=True, port=8000)