import sys
sys.path.insert(0, "/MyBudget")
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import app
from app  import *
from sys import dashboards



# =========  Layout  =========== #
content = html.Div(id="page-content")


app.layout = dbc.Container(children=[
    dbc.Row([
        dbc.Col([
           dcc.Location(id='url'),
           sidebar.layout 
        ],md=2, style={'background-color': 'purple','height': '1080px'}),
        dbc.Col([content],
          md=10, style={'background-color': 'blue','height': '1080px'})
    ])
], fluid=True,)

@app.callback(Output('page-content', 'children'),[('url', 'pathname')])
def render_page(pathname):
    if pathname=='/' or pathname == '/dashboards':
        return dashboards.layout
    if pathname == '/extratos':
        return extratos.layout
    if __name__ == '__main__':
        app.run_server(port=8051, debug=True)
