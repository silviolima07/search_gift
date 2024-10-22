from crewai import Task
import streamlit as st
from textwrap import dedent

from pydantic import BaseModel
from typing import List

class RecomendaOuput(BaseModel):
    recomendacoes: List[str]

def criar_task_recomendar(guia_compras):
    recomendar = Task(
        description=(
        "Usar a ferramenta de busca e pesquisar no site {site},  3 presentes {tipo}  para {genero}, custo abaixo de {preco}."
        #'Usar a ferramenta de busca para pesquisar apenas no site {site} e apresentar 3 presentes para menino.'
        
             ),
         expected_output=
             "Mostar 3 sugestões de  presentes. Mostrar em Português do Brasil." , 
         agent=guia_compras,
         output_file='lista_resultado.md'
         )
    return recomendar
