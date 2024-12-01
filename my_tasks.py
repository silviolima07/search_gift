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
    "Retorne o resultado com Nome, Descrição e Preço. Apenas salve a resposta em Portugues, um arquivo formato Markdown (md)."
    "Presentes recomendados:\n"
    "1)Nome:\nDescricao:\nPreço:\n"
             ),
         #expected_output=(
    #"Um arquivo Markdown (md) com 1 presente recomendado2, seguir o exemplo:"
    #"### Presentes recomendados:\n"
    #"#### 1) Nome:\n  #### Descricao:\n  #### Preço:\n"
    #        ), 
        expected_output = 
        """ Um dicionario com as informações de 3 presentes recomendados:
{
"nome": <nome>,
"descricao": <descricao>,
"preco": <preço>
} """,
        
         agent=guia_compras,
         #tools = [serper_tool],
         output_file='LISTA_PRESENTES.md'
         )
