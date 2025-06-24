import pandas as pd
import numpy as np
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
import dash
from dash import Dash, dcc, html

pio.renderers.default ='browser'

data = pd.read_csv('../Dash_Plotly/global_cancer_patients_2015_2024.csv')
print(f'data: {data}')

## tableau de board
fig1 = go.Figure()

# bar
fig1.add_trace(go.Bar(x=data['Gender'],y=data['Age'],marker_color='indianred', 
                      marker=dict(line=dict(color='blue', width=1.5)), name='Age'))
fig1.update_layout(title='Age en fonction du sexe',xaxis_title='Sexe', yaxis_title='Age')
fig1.show()
app = Dash(__name__)

app.layout = html.Div(
    children=[
        dcc.Dropdown(
            id='dropdown',
            options=[
                {'label': 'Year', 'value': 2010}
                ]),
        html.H3('Relation entre age et le sexe', style={"textAlign":'center', "font-size":20}),
        html.P("Tableau interactive de l'age en fonction du sexe", style={"font-size":10}),
        dcc.Graph(figure=fig1)

    ]
)


app.layout






























if __name__=='__main__':
    app.run(debug=True, port=8051)