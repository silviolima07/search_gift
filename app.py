# https://discuss.streamlit.io/t/the-sqlite3-version-3-34-1-on-streamlit-cloud-is-too-old-could-you-upgrade-it/48019
import pysqlite3
import sys 
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import pandas as pd
import streamlit as st
from crewai import Crew, Process
from my_agents import guia_compras, llm
from my_tasks import recomendar
from dotenv import load_dotenv
#from MyLLM import MyLLM
import time
#llm = MyLLM.GROQ_LLAMA

# Carregar variáveis de ambiente
load_dotenv()
import os

flag = True
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
output_file = "lista_presentes.md"

qtd= 2 # total de presentes recomendados

# Função para validar e ler o arquivo
def validar_arquivo_markdown(file_path):
    if os.path.exists(file_path):  # Verifica se o arquivo existe
        print(f"✅ Arquivo gerado com sucesso: {file_path}")
        with open(file_path, "r", encoding="utf-8") as f:
            conteudo = f.read()
            #st.markdown("#### 📄 Conteúdo do arquivo:")
            st.markdown(conteudo)
    else:
        print(f"❌ Erro: O arquivo {file_path} não foi gerado.")


def validar_arquivo_csv(file_csv):
    if os.path.exists(file_csv):
        return pd.read_csv(file_csv)
    else:
        raise FileNotFoundError("O arquivo CSV não foi gerado pela Task.")


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
            genero = 'menino/criança'
            tipo='educativos'
    elif faixa == '5-10' and genero == 'Feminino':
            genero = 'menina/criança'
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
    site = dict_loja.get(loja)
    
    inputs = {
            'site': site,
            'genero':genero,
            'preco':preco,
            'tipo':tipo
            #'search_query': f"Usar a ferramenta de busca e pesquisar {url} na url {site} presentes {tipo} para {genero}"
        }
    
    busca= "Usar a ferramenta de busca e pesquisar no site"
    #st.markdown("#### "+str(f'{busca}'))

    busca= "Site:"
    #st.markdown("#### "+str(f'{site}'))
    
    busca= f"Pesquisar presente {tipo}  para {genero}."     
    #st.markdown("#### "+str(f'{busca}'))
    
    busca= f"Custo abaixo de R$ {preco}."     
    #st.markdown("#### "+str(f'{busca}'))
    
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
    
    #import time
    #from datetime import datetime, timedelta

    # Inicialize a sessão de estado para armazenar o horário da última execução
    #if "ultimo_click" not in st.session_state:
    #    st.session_state.ultimo_click = None  # Inicialmente, nenhum clique

    #if "result" not in st.session_state:
    #    st.session_state.result = None  # Para armazenar o resultado do crewai.kickoff

    # Configurar o tempo de espera em segundos
    #TEMPO_ESPERA = 60
    
    # Função que simula o processamento do CrewAI
    #def executar_kickoff():
    #    # Simula a chamada do CrewAI
    #    #time.sleep(5)  # Simula tempo de processamento
    #    result = crew.kickoff(inputs=inputs)
        # Exibe a resposta no Streamlit
    #    validar_arquivo_markdown(output_file)

    # Verificar se o botão deve estar habilitado
    #tempo_restante = 0
    #if st.session_state.ultimo_click:
    #    tempo_restante = TEMPO_ESPERA - (datetime.now() - st.session_state.ultimo_click).total_seconds()

    #habilitar_botao = tempo_restante <= 0

    # Botão de iniciar
    #if st.button("Iniciar", disabled=not habilitar_botao):
        # Salva o momento do clique
    #    st.session_state.ultimo_click = datetime.now()
        # Executa o modelo e salva o resultado
    #    st.session_state.result = executar_kickoff()

    # Exibe o resultado do modelo, se disponível
    #if st.session_state.result:
    #    st.success(st.session_state.result)

    # Mensagem de tempo restante
    #if not habilitar_botao:
    #    st.warning(f"O botão será habilitado novamente em {int(tempo_restante)} segundos.")
        # Aguarda o tempo restante e força o rerender
    #    time.sleep(tempo_restante)
    #    st.experimental_rerun()  # Recarrega a interface para habilitar o botão
    
    # Verifica se já passou 1 minuto desde o último clique
    #habilitar_botao = (
    #st.session_state.ultimo_click is None or datetime.now() - st.session_state.ultimo_click >= timedelta(minutes=1)
    #)
    
    # Botão para iniciar a execução
    #if st.button("Iniciar", disabled=not habilitar_botao):
    #    st.session_state.ultimo_click = datetime.now()  # Armazena o horário do clique
    #    st.session_state.result = executar_kickoff()  # Executa o kickoff

    # Exibir o resultado, se disponível
    #if st.session_state.result:
    #    st.success(st.session_state.result)

    # Mensagem para o usuário se o botão estiver desabilitado
    #if not habilitar_botao:
    #    tempo_restante = timedelta(minutes=1) - (datetime.now() - st.session_state.ultimo_click)
    #    segundos_restantes = int(tempo_restante.total_seconds())
    #    st.warning(f"O botão será habilitado novamente em {segundos_restantes} segundos.")
    #    st.experimental_rerun() 
       
    ##################################
    inputs = {
            'site': site,
            'genero':genero,
            'preco':preco,
            'tipo':tipo,
            'qtd': qtd
        }
    st.markdown("#### Prompt enviado pro modelo")
    st.write(f'\nUse o SerperDevTool para pesquisar somente no site {site} do Brasil.')
    st.write(f'Encontre e recomende no maximo {qtd} presentes {tipo} para {genero}, com valor abaixo de {preco}.')
    st.write(f'Resposta deve conter no máximo {qtd} items.')
    st.write(f'Não mostrar resposta na console, apenas salve resultado numa lista formato Markdown.')

    if st.button("INICIAR"):
    #    time.sleep(5)
    #    inputs = {
    #        'site': url,
    #        'genero':genero,
    #        'preco':preco,
    #        'tipo':tipo,
    #        'qtd': qtd
    #    }
        #st.markdown("### '+f"Usar a ferramenta de busca e pesquisar no site {site},  3 presentes {tipo}  para {genero}.")
        
        with st.spinner('Wait for it...searching and processing...wait please'):
            try:
                # Executa o Crew, o que deve agora acionar os agentes e tasks
                result = crew.kickoff(inputs=inputs)  # Faz a chamada ao crew.kickoff
                
                #arquivo = validar_arquivo_csv('presentes.csv')
                #df = pd.read_csv(arquivo)
                #st.table(df)
                #st.write(result.token_usage)
                
                
                # Exibe a resposta no Streamlit
                st.markdown(f"### Lista de Presentes recomendados")
                #st.markdown(result)  # Função que processa e exibe a resposta
                # Chamada da função para validar
                #st.write(output_file)
                validar_arquivo_markdown(output_file.lower())
                st.success("Parabéns. Espere 60 segundos antes de executar novamente.")
                st.info("Se não aguardar, numero de tokens por minuto (TPM) pode ser ultrapassado e irá falhar.")
                st.write("Total Tokens consumidos: prompt + completion", result.token_usage.total_tokens)
                st.write('Prompt tokens enviados:', result.token_usage.prompt_tokens)
                st.write('Completion token gerados:', result.token_usage.completion_tokens)
                #flag = False
                #st.write(flag)
                time.sleep(60)
                st.write("Liberado executar novamente")
                time.sleep(5)
                
            except Exception as e:
                st.error(f"Error no crew.kickoff: {e}")
           
if option == 'About':
    st.markdown("### Sugestão de presentes educativos, interessantes e uteís.")
    st.markdown("### Este aplicativo faz uma busca e sugere 3 presentes de acordo com os critéros definidos.")
    st.markdown("### Modelo llama acessado via Groq.")

