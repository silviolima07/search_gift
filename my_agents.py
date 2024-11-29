from crewai import Agent
from crewai_tools import SerperDevTool

import streamlit as st

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
 

    
    
    
