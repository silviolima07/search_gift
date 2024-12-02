from crewai import Task
import streamlit as st
from my_agents import guia_compras
from crewai_tools import SerperDevTool
import json
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
        """
        Use o SerperDevTool para pesquisar somente no site {site} do Brasil. 
        Encontre e recomende 1 presente {tipo} para {genero}, com valor abaixo de {preco}. 
        Retorne o resultado em um arquivo CSV com as colunas:Nome , Descrição minima  e Preço dos presentes.
        Apresenta na saída o resultado.
        """
    ),
    expected_output=(
        """
        Um arquivo CSV contendo as informações de 1 presente recomendado com as colunas:
        Nome, Descrição e Preço.
        """ ),
    agent=guia_compras,
    tools=[serper_tool],  # Ferramenta configurada
    output_file="presentes.csv"  # Salvar diretamente como CSV
)




