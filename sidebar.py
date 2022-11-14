from multiprocessing.dummy import active_children
import os
from turtle import width

from matplotlib import style
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import app as app

from datetime import datetime, date
import plotly.express as px
import numpy as np
import pandas as pd






# ========= Layout ========= #
layout= dbc.Col([
    html.H1("Mybudget", className='text-primary'),
    html.P("Lucas", className='text-info'),
    html.Hr(),
    dbc.Button(id='botao_avatar',
               children=[html.Img(src='/assets/img_hom.png', id='avatar_change', alt='avatar', className='perfil_avatar',)
    ],style={'background-color': 'transparent', 'border-color':'transparent'}),
    #Seção novo #_____________________  
    dbc.Row([
        dbc.Col([
            dbc.Button(color='sucess', id='open-novo-receita',
                       children=['+Receita'])
        ], width=6),
            dbc.Col([
                dbc.Button(color='danger', id='open-novo-despesas',
                       children=['- Despesas'])
            ], width=6)
    ]),
    #Seção Receita #_____________________  
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle('Adicionar Receita')),
            dbc.ModalBody([
                dbc.Row([
                    dbc.Col([
                    dbc.Label('Descrição:'),
                    dbc.Input(placeholder="Ex.: dividendos, salário...", id="txt-receita"),
                    ], width=6),
                    dbc.Col([
                        dbc.Label("valor:"),
                        dbc.Input(placeholder="$100.00", id="valor_receita", value="")
                    ], width=6)
                ]),
            dbc.Row([
                dbc.Col([
                    dbc.Label("Data:"),
                    dcc.DatePickerSingle(id='date-receitas',
                                         min_date_allowed=date(2020,1,1),
                                         max_date_allowed=date(2030,12,31),
                                         date=datetime.today(),
                                         style={"width":"100%"}
                                        ),
                ], width=4),
                
                dbc.Col([dbc.Label("Extras"),
                         dbc.Checklist(
                             options=[],
                             value=[],
                             id='switches-input-receita',
                             switch=True
                            )
                ], width=4),
                dbc.Col([
                    html.Label('Categoria da receita'),
                    dbc.Select(id='select_receita', options=[], value=[])
                ], width=4)
                ], style={'margin-top': '25px'}),
            
            dbc.Row([
                dbc.Accordion([
                    dbc.AccordionItem(children=[
                        dbc.Row([
                            dbc.Col([
                                html.Legend("Adicionar Categoria", style={'color':'green'}),
                                dbc.Input(type="text", placeholder="nova categoria...", id="input-add-receita", value=""),
                                html.Br(),
                                dbc.Button("Adicionar", className="btn btn-sucess", id="add-category-receita", style={"margin-top":"20px"}),
                                html.Br(),
                                html.Div(id="category-div-add-receita", style={}),
                            ],width=6),
                            dbc.Col([
                                html.Legend('Excluir categorias', style={'color':'red'}),
                                dbc.Checklist(
                                    id='checklist-selected-style-receita',
                                    options=[],
                                    value=[],
                                    label_checked_style={'color':'red'},
                                    input_checked_style={'backgroundColor':'blue','borderColor':'orange'},
                                ),
                                dbc.Button ('Remover', color='warning', id='remove-category-receita', style={'margin-top':'20px'}),
                            ],width=6)
                        ])
                    ], title='Adicionar/Remover Categorias')
                ], flush=True, start_collapsed=True, id='accordion-receita'),
                html.Div(id='id_teste_receita', style={'padding-top':'20px'}),
                dbc.Modal([
                    dbc.Button("Adicionar Receita", id="salvar_receita", color="sucess"),
                    dbc.Popover(dbc.PopoverBody("Receita Salva"), target="salvar_receita", placement="left", trigger="click"),
                ])
            ], style={'margin-top': '25px'})
            ])
    ], style={"background-color":"rgba(17,140,79,0.05)"}, 
              id='modal-novo-receita',
              size="lg",
              is_open=False,
              centered=True,
              backdrop=True),
    #Seção Despesa #_____________________  
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle('Adicionar Despesa')),
        dbc.ModalBody([
            dbc.Row([
                dbc.Col([
                    dbc.Label('Descriçãp:'),
                    dbc.Input(placeholder="Ex.: Cartão, Net...", id="txt-despesa"),
                ], width=6),
                dbc.Col([
                    dbc.Label("Valor:"),
                    dbc.Input(placeholder="$100.00", id="valor_despesa"),
                ],width=6),
            ]),
        dbc.Row([
            dbc.Col([
                dbc.Label("Data:"),
                dcc.DatePickerSingle(id='date-despesas',
                min_date_allowed=date(2020,1,1),
                max_date_allowed=date(2030,12,31),
                date=datetime.today(),
                style={"width":"100%"}
                ),
            ],width=4),
            dbc.Col([dbc.Label("Extras"),
                     dbc.Checklist(
                         options=[],
                         value=[],
                         id='switches-input-despesas',
                         switch=True
                     )
                    ],  width=4),
            dbc.Col([
                    html.Label('Categoria da Despesa'),
                    dbc.Select(id='select_Despesas', options=[], value=[])
                ], width=4)
        ], style={'margin-top': '25px'}),
        dbc.Row([
            dbc.Accordion([
                dbc.AccordionItem(children=[
                   dbc.Row([
                            dbc.Col([
                                html.Legend("Adicionar Categoria", style={'color':'green'}),
                                dbc.Input(type="text", placeholder="nova categoria...", id="input-add-despesas", value=""),
                                html.Br(),
                                dbc.Button("Adicionar", className="btn btn-danger", id="add-category-despesas", style={"margin-top":"20px"}),
                                html.Br(),
                                html.Div(id="category-div-add-despesas", style={}),
                            ],width=6),
                            dbc.Col([
                                html.Legend('Excluir categorias', style={'color':'red'}),
                                dbc.Checklist(
                                    id='checklist-selected-style-despesas',
                                    options=[],
                                    value=[],
                                    label_checked_style={'color':'red'},
                                    input_checked_style={'backgroundColor':'blue','borderColor':'orange'},
                                ),
                                dbc.Button ('Remover', color='warning', id='remove-category-despesas', style={'margin-top':'20px'}),
                            ],width=6)
                        ]) 
                ],title='Adicionar/Remover categorias')
            ],flush=True, start_collapsed=True, id='accordion-despesa'),
                html.Div(id='id_teste_receita', style={'padding-top':'20px'}),
                dbc.Modal([
                    dbc.Button("Adicionar Receita", id="salvar_receita", color="sucess"),
                    dbc.Popover(dbc.PopoverBody("Receita Salva"), target="salvar_receita", placement="left", trigger="click"),
                ])           
        ], style={'margin-top':'25px'})
        ])
    ],  style={"background-color":"rgba(17,140,79,0.05)"},
        id='modal-novo-Despesa',
        size="lg",
        is_open=False,
        centered=True,
        backdrop=True),    
    #Seção NAV #_____________________  
    html.Hr(),
    dbc.Nav(
        [dbc.NavLink("dashboards",href="/dashboards", active="exact"),
         dbc.NavLink("extratos",href="/extratos", active="exact"),            
        ], vertical=True, pills=True, id='nav_buttons', style={"margin-bottom":"50px"}),
    ])
     

                                  
    


# =========  Callbacks  =========== #
# Pop-up receita
@app.callback(
    Output('modal-novo-receita', 'is_open'),
    Input('open-novo-receita', 'n_clicks'),
    State('modal-novo-receita', 'is_open')
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open
# Pop-up despesa
@app.callback(
    Output('modal-novo-despesa', 'is_open'),
    Input('open-novo-despesa', 'n_clicks'),
    State('modal-novo-despesa', 'is_open')
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open
