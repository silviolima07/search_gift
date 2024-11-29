from crewai import Agent

import crewai_tools

from crewai_tools import SerperDevTool

from MyLLM import MyLLM

from dotenv import load_dotenv
# Carregar variáveis de ambiente
load_dotenv()

import os

load_dotenv()

# Obter a chave da API GROQ
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Definir o modelo de linguagem
llm = MyLLM.GROQ_LLAMA



# Initialize the tool for internet searching capabilities
serper_tool = SerperDevTool()

# Configuração do agente

   
guia_compras = Agent(
        role="guia de compras",
        goal="Orientar pessoas que fazem compras.",
        backstory=
            "Você é responsável por orientar na melhor compra."   
        ,
        llm=llm, # estava provider=provider
        verbose=True,
        memory=False
        #tools=[serper_tool]
    )

    
    
    
