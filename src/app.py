import streamlit as st
import numpy as np
import joblib

# Criando um frontend usando streamlit que usa o Scaler e Modelo importados do Jupyter Notebook

scaler = joblib.load("src\Scaler.pkl")

st.set_page_config(layout = "centered")

st.title("Previsor de Avaliação de Restaurantes")
st.caption("Um sistema que utiliza técnicas de Machine Learning e Mineração de Dados para prever a avaliação e desempenho de restaurantes.")

st.divider()

averagecost = st.number_input("Informe o valor estimado para dois", min_value = 30, max_value=9999, value = 100, step = 50)
tablebooking = st.selectbox("O restaurante tem um sistema de reservas?", ["Sim", "Não"])
onlinedelivery = st.selectbox("O restaurante faz delivery?", ["Sim", "Não"])
pricerange = st.selectbox("Qual é a faixa de preço do restaurante em relação aos concorrentes? (1 sendo Muito Baixa, 4 sendo Muito Alta)", [1, 2, 3, 4])

predicbutton = st.button("Preveja a review do restaurante!")

st.divider()

model = joblib.load("src\mlmodel.pkl")

bookingstatus = 1 if tablebooking == "Sim" else 0
deliverystatus = 1 if onlinedelivery == "Sim" else 0

values = [[averagecost, bookingstatus, deliverystatus, pricerange]]
my_X_values = np.array(values)
X = scaler.transform(my_X_values)

if predicbutton:
    prediction = model.predict(X)[0]
    if prediction < 2.5:
        st.write(f"A avaliação dos clientes provavelmente será ruim. Nota Estimada: {prediction:.2f}")
    elif prediction < 3.5:
        st.write(f"A avaliação dos clientes provavelmente será  mediana. Nota Estimada: {prediction:.2f}")
    elif prediction < 4:
        st.write(f"A avaliação dos clientes provavelmente será boa! Nota Estimada: {prediction:.2f}")
    elif prediction < 4.5:
        st.write(f"A avaliação dos clientes provavelmente será  muito boa! Nota Estimada: {prediction:.2f}")
    else:
        st.write(f"A avaliação dos clientes provavelmente será exelente! Nota Estimada: {prediction:.2f}")