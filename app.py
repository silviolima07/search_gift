# https://discuss.streamlit.io/t/the-sqlite3-version-3-34-1-on-streamlit-cloud-is-too-old-could-you-upgrade-it/48019
#import pysqlite3
import sys 
#sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import pandas as pd
import streamlit as st
from crewai import Crew, Process
from my_agents import guia_compras, llm
from my_tasks import recomendar
from dotenv import load_dotenv
#from MyLLM import MyLLM

#llm = MyLLM.GROQ_LLAMA

# Carregar variáveis de ambiente
load_dotenv()
import os

# Verifica se as chaves estão acessíveis
#assert os.getenv("OPENAI_API_KEY"), "OPENAI_API_KEY não está configurada!"
assert os.getenv("GROQ_API_KEY"), "GROQ_API_KEY não está configurada!"
assert os.getenv("SERPER_API_KEY"), "SERPER_API_KEY não está configurada!"

from PIL import Image
#import litellm  # Importando o LiteLLM para usar o Groq
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", message="Overriding of current TracerProvider is not allowed")

# Nome do arquivo gerado pela task
output_file = "LISTA_PRESENTES.md"

# Função para validar e ler o arquivo
def validar_arquivo_markdown(file_path):
    if os.path.exists(file_path):  # Verifica se o arquivo existe
        print(f"✅ Arquivo gerado com sucesso: {file_path}")
        with open(file_path, "r", encoding="utf-8") as f:
            conteudo = f.read()
            st.markdown("#### 📄 Conteúdo do arquivo:")
            st.markdown(conteudo)
    else:
        print(f"❌ Erro: O arquivo {file_path} não foi gerado.")

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


img0 = Image.open("img/3_gift.png")
st.image(img0, caption="", use_container_width=True)

html_page_title = """
    <div style="background-color:black;padding=60px">
        <p style='text-align:center;font-size:50px;font-weight:bold'>Presente Pra Ti</p>
    </div>
"""
st.markdown(html_page_title, unsafe_allow_html=True)

img = Image.open("img/gift2.png")
st.sidebar.image(img, caption="", use_container_width=True)

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
    #st.write("Loja:", dict_loja.get(loja))
    
    html_page_crewai = """
    <div style="background-color:black;padding=60px">
        <p style='text-align:center;font-size:40px;font-weight:bold'>Sugestões de Presentes</p>
    </div>
    """
    st.markdown(html_page_crewai, unsafe_allow_html=True)
    
    #url = "https://loja.imaginarium.com.br/"
    url = dict_loja.get(loja)
    
    inputs = {
            'site': url,
            'genero':genero,
            'preco':preco,
            'tipo':tipo
            #'search_query': f"Usar a ferramenta de busca e pesquisar {url} na url {site} presentes {tipo} para {genero}"
        }

    busca= "Usar a ferramenta de busca e pesquisar no site"
    st.markdown("#### "+str(f'{busca}'))

    busca= "Site:"
    st.markdown("#### "+str(f'{url}'))
    
    busca= f"Pesquisar 3 presentes {tipo}  para {genero}."     
    st.markdown("#### "+str(f'{busca}'))
    
    busca= f"Custo abaixo de R$ {preco}."     
    st.markdown("#### "+str(f'{busca}'))
    
    # Configuração do CrewAI com o Groq via LiteLLM
    # Aqui estamos passando o provider diretamente para o agente e task
    #provider = groq_provider()  # Usando o provider do Groq
    #llm = llama # provider groq
       
    #st.write("Agente guia_compras ok")
    #recomendar = recomendar
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
    from crewai import LLM         
    st.write("LLM: ", llm.model)
    #st.write("LLM: ", dir(llm.model))
    #teste = LLM(model=llm.model)
    #st.write("Max tokens: ", dir(llm.max_tokens))
    #st.write("Max completion tokens: ", getattr(teste, 'max_tokens','limite nao especificado'))
    #st.write("Atributes: ", dir(teste))

    ##################################
    import time
    from datetime import datetime, timedelta

    # Inicialize a sessão de estado para armazenar o horário da última execução
    if "ultimo_click" not in st.session_state:
        st.session_state.ultimo_click = None  # Inicialmente, nenhum clique

    if "result" not in st.session_state:
        st.session_state.result = None  # Para armazenar o resultado do crewai.kickoff

    # Configurar o tempo de espera em segundos
    TEMPO_ESPERA = 60
    
    # Função que simula o processamento do CrewAI
    def executar_kickoff():
        # Simula a chamada do CrewAI
        time.sleep(5)  # Simula tempo de processamento
        #result = crew.kickoff(inputs=inputs)
        # Exibe a resposta no Streamlit
        #validar_arquivo_markdown(output_file)

    # Verificar se o botão deve estar habilitado
    tempo_restante = 0
    if st.session_state.ultimo_click:
        tempo_restante = TEMPO_ESPERA - (datetime.now() - st.session_state.ultimo_click).total_seconds()

    habilitar_botao = tempo_restante <= 0

    # Botão de iniciar
    if st.button("Iniciar", disabled=not habilitar_botao):
        # Salva o momento do clique
        st.session_state.ultimo_click = datetime.now()
        # Executa o modelo e salva o resultado
        st.session_state.result = executar_modelo()

    # Exibe o resultado do modelo, se disponível
    if st.session_state.result:
        st.success(st.session_state.result)

    # Mensagem de tempo restante
    if not habilitar_botao:
        st.warning(f"O botão será habilitado novamente em {int(tempo_restante)} segundos.")
        # Aguarda o tempo restante e força o rerender
        time.sleep(tempo_restante)
        st.experimental_rerun()  # Recarrega a interface para habilitar o botão
    """
    # Verifica se já passou 1 minuto desde o último clique
    #habilitar_botao = (
    st.session_state.ultimo_click is None or datetime.now() - st.session_state.ultimo_click >= timedelta(minutes=1)
    )

    # Botão para iniciar a execução
    if st.button("Iniciar", disabled=not habilitar_botao):
        st.session_state.ultimo_click = datetime.now()  # Armazena o horário do clique
        st.session_state.result = executar_kickoff()  # Executa o kickoff

    # Exibir o resultado, se disponível
    if st.session_state.result:
        st.success(st.session_state.result)

    # Mensagem para o usuário se o botão estiver desabilitado
    if not habilitar_botao:
        tempo_restante = timedelta(minutes=1) - (datetime.now() - st.session_state.ultimo_click)
        segundos_restantes = int(tempo_restante.total_seconds())
        st.warning(f"O botão será habilitado novamente em {segundos_restantes} segundos.")
        st.experimental_rerun() 
     """   
    ##################################
    """
    if st.button("INICIAR"):
        inputs = {
            'site': url,
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
                #st.markdown(f"### Presentes recomendados")
                #st.markdown(result)  # Função que processa e exibe a resposta
                # Chamada da função para validar
                validar_arquivo_markdown(output_file)
                
            except Exception as e:
                st.error(f"Error no crew.kickoff: {e}")
    """       
if option == 'About':
    st.markdown("### Sugestão de presentes educativos, interessantes e uteís.")
    st.markdown("### Este aplicativo faz uma busca e sugere 3 presentes de acordo com os critéros definidos.")
    st.markdown("### Modelo llama acessado via Groq.")

