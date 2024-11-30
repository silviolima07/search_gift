import streamlit as st

def selecionar_modelo():
    modelo = st.radio(
    "Modelos",
    ["GROQ_LLAMA", "GROQ_MIXTRAL", "OpenAI"],
    captions=[
        "llama3-70b-8192",
        "mixtral-8x7b-32768",
        "gpt-4o-mini",
    ])
    st.write("Modelo selecionado:", modelo)
    return modelo
	