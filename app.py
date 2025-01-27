import streamlit as st

st.header("Calculadora",deLimiter="gray")

st.write("Expressão matemática:")
expression = st.text_input("Entre com a expressão:")

if expression:
    try:
        result = eval(expression)
        st.write(f"Resultado: {result}")
