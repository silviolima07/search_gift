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

from crewai import Task
import streamlit as st
from my_agents import guia_compras
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
import os
import pandas as pd

# Carregar variáveis de ambiente
load_dotenv()

SERPER_API_KEY = os.getenv('SERPER_API_KEY')

# Inicializar a ferramenta de busca
serper_tool = SerperDevTool()
serper_tool.n_results = 10

# Configuração da Task
recomendar = Task(
    description=(
        "Use a ferramenta de busca para pesquisar somente no site {site}. "
        "Encontre 3 presentes {tipo} para {genero}, com valor abaixo de {preco}, disponíveis no Brasil. "
        "Retorne o resultado com Nome, Descrição e Preço em formato de dicionário. Exemplo de resposta:\n"
        "{\n"
        "  'Nome': <nome>,\n"
        "  'Descricao': <descricao>,\n"
        "  'Preço': <preço>\n"
        "}"
    ),
    expected_output=(
        "Um dicionário com as informações de 3 presentes recomendados. Exemplo:\n"
        "{\n"
        "  'Nome': [<nome1>, <nome2>, <nome3>],\n"
        "  'Descricao': [<descricao1>, <descricao2>, <descricao3>],\n"
        "  'Preço': [<preco1>, <preco2>, <preco3>]\n"
        "}"
    ),
    agent=guia_compras,
    output_file = 'presentes.csv'     
    tools=[serper_tool],  # Ferramenta configurada
)




