import pandas as pd
import streamlit as st
from crewai import Crew, Process
from my_agents import criar_agente_guia_compras
from my_tasks import criar_task_recomendar
from config_llm import llama
import os
from PIL import Image
#import litellm  # Importando o LiteLLM para usar o Groq
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", message="Overriding of current TracerProvider is not allowed")

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider

trace.set_tracer_provider(TracerProvider())
trace.set_tracer_provider(None)

import logging
logging.basicConfig(level=logging.DEBUG)

def selecionar_genero():
    genero = st.radio(
    "Escolha:",
    ["Masculino", "Feminino"],
    horizontal = True
    )
    return genero
    
def selecionar_loja():
    loja = st.radio(
    "Loja Online:",
    ["Amazon", "Imaginarium", 'Mercado Livre'],
    horizontal = True
    )
    return loja



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

# # Função para exibir a resposta no Streamlit
# def exibir_resposta(result):
    # if 'choices' in result and len(result['choices']) > 0:
        # content = result['choices'][0]['message']['content']
        # st.markdown(content)  # Exibe o conteúdo retornado pela API
    # else:
        # st.error("A resposta não contém o conteúdo esperado.")

# Interface de Streamlit

img0 = Image.open("img/3_gift.png")
st.image(img0, caption="", use_column_width=True)

html_page_title = """
    <div style="background-color:black;padding=60px">
        <p style='text-align:center;font-size:50px;font-weight:bold'>Presente Pra Ti</p>
    </div>
"""
st.markdown(html_page_title, unsafe_allow_html=True)

img = Image.open("img/gift2.png")
st.sidebar.image(img, caption="", use_column_width=True)

st.sidebar.markdown("# Menu")
option = st.sidebar.selectbox("Menu", ["Pesquisar", 'About'], label_visibility='hidden')

if option == 'Pesquisar':
    st.markdown("### Selecione gênero:")
    genero = selecionar_genero()

    
    st.markdown("### Idade Aproximada:")
    faixa = st.radio("Anos  ",['5-10','15-20','30-40'], 
    captions=[
        "criança",
        "adolescente",
        "adulto",
    ],
    horizontal = True)
    
    if faixa == '5-10' and genero == 'Masculino':
            genero = 'menino'
            tipo='educativos'
    elif faixa == '5-10' and genero == 'Feminino':
            genero = 'menina'
            tipo='educativos'
    elif faixa == '15-20' and genero == 'Masculino':
            genero = 'menino adolescente '
            tipo='interessantes'
    elif faixa == '15-20' and genero == 'Feminino':
            genero = 'uma menina adolescente'
            tipo='interessantes'
    elif faixa == '30-40' and genero == 'Masculino':
            genero = 'homem'
            tipo='uteis'
    else:
            genero = 'mulher'
            tipo='uteis'
    
    st.markdown("### Abaixo de:")
    preco = st.radio("Preço  ",[50, 100, 200, 300,400,500], horizontal = True)
    
    #st.markdown("### Quantas recomendações de lugares deseja:")
    #total_items = st.radio(" ", [1, 2, 3, 4, 5], horizontal=True)
    
    dict_loja = {'Amazon':'https://amazon.com.br', 'Imaginarium': 'https://loja.imaginarium.com.br/', 'Mercado Livre': 'https://mercadolivre.com.br'}   
    loja = selecionar_loja()        
    st.write("Loja:", dict_loja.get(loja))
    
    html_page_crewai = """
    <div style="background-color:black;padding=60px">
        <p style='text-align:center;font-size:40px;font-weight:bold'>3 Sugestões de Presentes</p>
    </div>
    """
    st.markdown(html_page_crewai, unsafe_allow_html=True)
    
    #url = "https://loja.imaginarium.com.br/"
    url = dict_loja.get(loja)
    
    inputs = {
            'site': url,
            'genero':genero,
            'preco':preco,
            'tipo':tipo,
            'search_query': f"Usar a ferramenta de busca e pesquisar {url} na url {site} presentes {tipo} para {genero}"
        }
    busca= f"Usar a ferramenta de busca e pesquisar em {site}"
    st.markdown("#### "+str(f'{busca}'))
    
    busca= f"Pesquisar 3 presentes {tipo}  para {genero}."     
    st.markdown("#### "+str(f'{busca}'))
    
    busca= f"Custo abaixo de R$ {preco}."     
    st.markdown("#### "+str(f'{busca}'))
    
    # Configuração do CrewAI com o Groq via LiteLLM
    # Aqui estamos passando o provider diretamente para o agente e task
    #provider = groq_provider()  # Usando o provider do Groq
    llm = llama # provider groq
       
    #st.write(type(llm))
    #st.write("Mdelo llm ok")
    guia_compras = criar_agente_guia_compras(llm) 
    #st.write("Agente guia_compras ok")
    recomendar = criar_task_recomendar(guia_compras)  
    #st.write("Task recomendar ok")
    
    #st.markdown("## Aperte os cintos e boa viagem")
    
    # Certifique-se de que a Crew está configurada corretamente
    crew = Crew(
        agents=[guia_compras],
        tasks=[recomendar],
        process=Process.sequential,  # Processamento sequencial das tarefas
        verbose=True,  # Verbose para depuração
        #max_rpm=30,
        cache=True
        #max_iterations=10,  # Aumente o número de iterações se necessário
        #time_limit_seconds=300  # Ajuste o limite de tempo (em segundos)
    )
             
    
    
    #with col2:
    #    if estado == 'Bahia':
    #        img_estado = Image.open("img/bahia.png")
    #    elif estado == 'Rio de Janeiro':
    #        img_estado = Image.open("img/rio_de_janeiro.png")
    #    elif estado == 'Ceará':
    #        img_estado = Image.open("img/ceara.png")
    #    elif estado == 'Santa Catarina':
    #        img_estado = Image.open("img/santa_catarina.png")  
    #    elif estado == 'Pernambuco':
    #        img_estado = Image.open("img/pernambuco.png")    
        
     #   st.image(img_estado, caption="", use_column_width=False)

    if st.button("INICIAR"):
        inputs = {
            'site':' https://loja.imaginarium.com.br/',
            'genero':genero,
            'preco':preco,
            'tipo':tipo,
            'search_query': f"Usar a ferramenta de busca e pesquisar na url {'site'} presentes para menino de 5 anos"
        }
        #st.markdown("### '+f"Usar a ferramenta de busca e pesquisar no site {site},  3 presentes {tipo}  para {genero}.")
        
        with st.spinner('Wait for it...searching and processing...wait please'):
            try:
                # Executa o Crew, o que deve agora acionar os agentes e tasks
                result = crew.kickoff(inputs=inputs)  # Faz a chamada ao crew.kickoff
                
                # Exibe a resposta no Streamlit
                #st.markdown(f"### Resultado para {estado}")
                st.markdown(result)  # Função que processa e exibe a resposta
                
            except Exception as e:
                st.error(f"Error no crew.kickoff: {e}")
                
if option == 'About':
    st.markdown("### Sugestão de presentes educativos, interessantes e uteís.")
    st.markdown("### Este aplicativo faz uma busca e sugere 3 presentes de acordo os critéros defimidos.")
    st.markdown("### Modelo llama acessado via Groq.")

