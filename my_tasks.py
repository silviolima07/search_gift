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
        Use o SerperDevTool para pesquisar somente no site {site}. 
        Encontre 3 presentes {tipo} para {genero}, com valor abaixo de {preco}, disponíveis no Brasil. 
        Retorne o resultado com Nome do presente, Descrição da presente e Preço do presente em formato de dicionário.
        """
    ),
    expected_output=(
        """
        Um JSON válido contendo as informações de 3 presentes recomendados:
        {
            "Nome": ["<nome1>", "<nome2>", "<nome3>"],
            "Descricao": ["<descricao1>", "<descricao2>", "<descricao3>"],
            "Preco": ["<preco1>", "<preco2>", "<preco3>"]
        }
        """
    ),
    agent=guia_compras,
    output_file='presentes.json',
    tools=[serper_tool],  # Ferramenta configurada
)




