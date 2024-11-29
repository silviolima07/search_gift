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


recomendar = Task(
        description=
        """
        Usar a ferramenta de busca e pesquisar apenas e somente no site {site},  3 presentes {tipo}  para {genero}, com preço abaixo de {preco}.
        Use a ferramenta SerperTool para buscar informações e listar os produtos encontrados.
        Sua resposta deve incluir:
        \n - Nome\n - Preço\n -\n Descrição. "
        "Certifique-se de listar pelo menos 3 produtos."
             """,
         expected_output=
             """
             Mostar 3 sugestões de  presentes. Mostrar em Português do Brasil.
             No seguinte formato:
             Presentes recomendados:
             1) nome: descricao e valor
             2) nome: descricao e valor
             3) nome: descricao e valor
             """ , 
         agent=guia_compras,
         #tools = [serper_tool],
         output_file='lista_resultado.md'
         )
