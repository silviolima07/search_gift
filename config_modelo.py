import streamlit as st

def selecionar_modelo():
    modelo = st.radio(
    "Modelos do Groq:",
    ["llama", "mixtral", "gemma"],
    captions=[
        "llama3-70b-8192",
        "mixtral-8x7b-32768",
        "gemma-7b-it",
    ])
    st.write("Modelo selecionado:", modelo)
    return modelo
	