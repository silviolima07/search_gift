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
        description=
        """
        Usar a ferramenta de busca e pesquisar apenas e somente no site {site}.
        Encontrar 3 presentes {tipo}  para {genero}, com preço abaixo de {preco}, pesquisar somente no Brasil.
        Sua resposta deve incluir: \nNome, \nDescrição \nPreço.
        Salvar num arquivo formato Markdown.
             """,
         expected_output=
             """
             Um arquio em formato Markdown (md) com as 3 sugestões de  presentes.
             Salvar o arquivo gerado no seguinte padrao:
             Presentes recomendados:
             1) 
             Nome: 
             Descricao:
             Preço:
             """ , 
         agent=guia_compras,
         #tools = [serper_tool],
         output_file='LISTA_PRESENTES.md'
         )
