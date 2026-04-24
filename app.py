import streamlit as st
import numpy as np
from scipy.stats import poisson

st.title("⚽ AI Betting Tester")

def ai_model():
    return np.array([0.52, 0.25, 0.23])

def poisson_model(h, a):
    home = draw = away = 0
    for i in range(6):
        for j in range(6):
            p = poisson.pmf(i, h) * poisson.pmf(j, a)
            if i > j:
                home += p
            elif i == j:
                draw += p
            else:
                away += p
    return np.array([home, draw, away])

def predict():
    ml = ai_model()
    px = poisson_model(1.6, 1.2)
    return (ml + px) / 2

odds_home = st.slider("Home odds", 1.2, 5.0, 2.1)
odds_draw = st.slider("Draw odds", 1.2, 5.0, 3.2)
odds_away = st.slider("Away odds", 1.2, 5.0, 3.5)

if st.button("RUN AI"):
    probs = predict()

    st.write("Home:", round(probs[0], 2))
    st.write("Draw:", round(probs[1], 2))
    st.write("Away:", round(probs[2], 2))

    values = [
        probs[0] * odds_home,
        probs[1] * odds_draw,
        probs[2] * odds_away
    ]

    best = np.argmax(values)

    if values[best] > 1:
        st.success(f"🔥 VALUE BET FOUND: option {best}")
    else:
        st.error("❌ No value bet")
