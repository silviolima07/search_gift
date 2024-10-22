# config.py
import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
#import litellm 
import openai

#from groq import Groq

# Carregar variáveis de ambiente
load_dotenv()



# Obter a chave da API GROQ
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

#litellm.set_verbose = True

# def groq_provider():
    # return litellm.completion(
        # model="groq/llama3-8b-8192",  # Certifique-se de que este é o modelo correto do Groq
        # messages=[
            # {"role": "system", "content": "Você é um guia turístico especializado."},
            # {"role": "user", "content": "Recomende os melhores pontos turísticos do Brasil."}
        # ],
        # #type="chat",  # Definindo como chat para o Groq
        # tools=[],
        # tool_choice="auto"
    # )

llama = ChatGroq(
             api_key=GROQ_API_KEY,
             model= "llama3-70b-8192"
         )
          

#from groq import Groq


#llama = "llama-3.1-8b-instant" # "groq/llama3-70b-8192"