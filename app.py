import streamlit as st

st.header("Calculadora")

st.write("Expressão matemática:")
expression = st.text_input("Entre com a expressão:")

if expression:
    try:
        result = eval(expression)
        st.write(f"Resultado: {result}")
    except Exception as e:
        st.write(f"Erro ao avaliar a expressão: {e}")
