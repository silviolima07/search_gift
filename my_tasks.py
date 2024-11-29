from crewai import Task
import streamlit as st

def criar_task_recomendar(guia_compras):
    recomendar = Task(
        description=(
        "Usar a ferramenta de busca e pesquisar apenas e somente no site {site},  3 presentes {tipo}  para {genero}, com preço abaixo de {preco}."
        #'Usar a ferramenta de busca para pesquisar apenas no site {site} e apresentar 3 presentes para menino.'
        
             ),
         expected_output=
             """
             Mostar 3 sugestões de  presentes. Mostrar em Português do Brasil.
             No seguinte formato:
             Presentes recomendados:
             1) presente: descricao e valor
             2) presente: descricao e valor
             3) presente: descricao e valor
             """ , 
         agent=guia_compras,
         output_file='lista_resultado.md'
         )
    return recomendar
