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


# Dicionario para rastrear as últimas consultas de cada termo
ultima_consulta_busca = {}
# Fun ção de cache personalizada
def funcao_cache ( args , resultado ) :
    termo = args[0] # Primeiro argumento é o termo de busca
    agora = datetime.now ()
    
    # Verifica se o termo foi consultado nos últimos 60 minutos
    if termo in ultima_consulta_busca :
        ultima_hora_consulta = ultima_consulta_busca [ termo ]
        if agora - ultima_hora_consulta < timedelta ( hours =1) :
            print("Usar cache")
            return True # cache se a última consulta foi menos de 1h
    ultima_consulta_busca [ termo ] = agora # última consulta
    print('Não usar cache')
    return False # Não armazena em cache se passou mais de 1 hora


# Associa a função de cache à ferramenta SerperDevTool
serper_tool.cache_function = funcao_cache


# Configuração da Task
recomendar = Task(
    description =""" 
Use o SerperDevTool para pesquisar somente no site {site} do Brasil. 
Encontre e recomende no maximo {qtd} presente {tipo} para {genero}, com valor abaixo de {preco}.
Resposta deve conter no máximo {qtd} items.
Não mostrar resposta na console, apenas salve resultado numa lista formato Markdown.
""" ,
    expected_output =
    """ 
        Nome: Nome do presente\n
        
        Descrição: Descrição do presente.\n
        
        Preço: Preço do presente
    """,
    agent=guia_compras,
    tools=[serper_tool],  # Ferramenta configurada
    output_file="lista_presentes.md"  # Salvar diretamente como CSV
)




