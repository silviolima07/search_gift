from crewai import Agent
from crewai_tools import SerperDevTool
#import litellm

import streamlit as st

# Defina a função do provedor Groq
# def groq_provider():
    # return litellm.completion(
        # model="groq/llama3-8b-8192",  # Certifique-se de que este é o modelo correto do Groq
        # messages=[
            # {"role": "system", "content": "Você é um guia turístico especializado."},
            # {"role": "user", "content": "Recomende os melhores pontos turísticos do Brasil."}
        # ],
        # #type="chat",
        # tools=[],
        # tool_choice="auto"
    # )

# Initialize the tool for internet searching capabilities
serper_tool = SerperDevTool()

# Configuração do agente

def criar_agente_guia_compras(provider):
    
    guia_compras = Agent(
        role="guia de compras",
        goal="Orientar pessoas que fazem compras.",
        backstory=
            "Você é responsável por orientar na melhor compra."   
        ,
        llm=provider, # estava provider=provider
        verbose=True,
        memory=False,
        tools=[serper_tool]
    )
    #st.markdown("#### Agente guia turistico sua mente sera o "+ str(provider.model))
    return guia_compras   
 

    
    
    
