import streamlit as st
from MyLLM import MyLLM


GROQ_LLAMA   = MyLLM.GROQ_LLAMA
GROQ_MIXTRAL = MyLLM.GROQ_MIXTRAL
OpenAI       = MyLLM.GPT4o_mini


def selecionar_modelo():
    modelo = st.selectbox(
    "Modelos",
    [GROQ_LLAMA, "GROQ_MIXTRAL", "OpenAI"],
    index= None,
    captions=[
        "llama3-70b-8192",
        "mixtral-8x7b-32768",
        "gpt-4o-mini",
    ])
    st.write("Modelo selecionado:", modelo)
    return modelo
	