import streamlit as st
import requests
import numpy as np

st.title("⚽ DAILY AI FOOTBALL TIPSTER")

# -----------------------------
# API (ingyenes demo kulcs kell később)
# -----------------------------
API_KEY = "YOUR_API_KEY"
url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"

headers = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

# mai meccsek lekérése
@st.cache_data
def get_matches():
    params = {"date": "2026-04-25"}  # MAI NAP (később auto is lehet)
    r = requests.get(url, headers=headers, params=params)
    data = r.json()

    matches = []
    for m in data["response"]:
        home = m["teams"]["home"]["name"]
        away = m["teams"]["away"]["name"]
        fixture_id = m["fixture"]["id"]
        matches.append((f"{home} vs {away}", fixture_id))

    return matches

# -----------------------------
# AI MODEL (egyszerűsített)
# -----------------------------
def ai_model(home, away):
    # később: xG + Elo + form
    return np.array([0.50, 0.25, 0.25])

def value(prob):
    return prob * 2.0 - 1  # fake odds baseline

# -----------------------------
# UI
# -----------------------------
st.subheader("📅 Today matches")

matches = get_matches()

if not matches:
    st.error("No matches found (API key kell)")
    st.stop()

labels = [m[0] for m in matches]
selected = st.selectbox("Select match", labels)

match_id = dict(matches)[selected]

if st.button("ANALYZE MATCH"):
    home, away = selected.split(" vs ")

    probs = ai_model(home, away)

    st.write("### 📊 AI Prediction")
    st.write(f"Home: {probs[0]:.2f}")
    st.write(f"Draw: {probs[1]:.2f}")
    st.write(f"Away: {probs[2]:.2f}")

    best = np.argmax(probs)
    tips = ["HOME WIN", "DRAW", "AWAY WIN"]

    st.success(f"🔥 TIP: {tips[best]}")

    if probs[best] > 0.55:
        st.success("VALUE BET POSSIBILITY 🔥")
    else:
        st.warning("NO EDGE / SKIP ❌")
