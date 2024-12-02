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
    description =""" 
Use o SerperDevTool para pesquisar somente no site {site} do Brasil. 
Encontre e recomende 2 presentes {tipo} para {genero}, com valor abaixo de {preco}. 
Não mostrar resposta na console, apenas salve resultado numa lista formato Markdown.
""" ,
    expected_output =
    """
        Uma lista formatada em Markdown com as informações dos presentes:
        - **1)Nome:** [Nome do presente]
        - **Descrição:** Breve descrição do presente.
        - **Preço:** Valor do presente
        - **2)Nome:** [Nome do presente]
        - **Descrição:** Breve descrição do presente.
        - **Preço:** Valor do presente
    """,
    agent=guia_compras,
    tools=[serper_tool],  # Ferramenta configurada
    output_file="lista_presentes.md"  # Salvar diretamente como CSV
)




