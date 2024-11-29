# config.py
import os
from dotenv import load_dotenv

from groq import Groq

# Carregar variáveis de ambiente
load_dotenv()

groq = Groq

# Obter a chave da API GROQ
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

llama = "groq/llama-3.1-70b-versatile' #llama3-70b-8192"
      
