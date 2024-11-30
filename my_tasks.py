from crewai import Task
import streamlit as st
from my_agents import guia_compras
from crewai_tools import SerperDevTool

from dotenv import load_dotenv
import os

load_dotenv()

SERPER_API_KEY = os.getenv('SERPER_API_KEY')

# Initialize the tool for internet searching capabilities
serper_tool = SerperDevTool()
serper_tool.n_results = 10


recomendar = Task(
        description=(
    "Use a ferramenta de busca para pesquisar somente no site {site}. "
    "Encontre 3 presentes {tipo} para {genero}, com valor abaixo de {preco}, disponíveis no Brasil. "
    "Retorne o resultado com Nome, Descrição e Preço. Apenas salve a resposta em um arquivo Markdown (md) no seguinte formato:"
    "### Presentes recomendados:\n"
    "1)### Nome:\n    ### Descricao:\n    ### Preço:\n"
             ),
         expected_output=(
    "Um arquivo Markdown (md) com 3 presentes recomendados, formatado assim:"
    "### Presentes recomendados:\n"
    "#### 1) Nome:\n  #### Descricao:\n  #### Preço:\n"
            ), 
         agent=guia_compras,
         #tools = [serper_tool],
         output_file='LISTA_PRESENTES.md'
         )
