import streamlit as st
import numpy as np

st.title("⚽ AI Football Tip Generator")

# --- DEMO MATCH LIST (később API-val cseréljük) ---
matches = [
    "Arsenal vs Chelsea",
    "Real Madrid vs Barcelona",
    "Bayern vs Dortmund"
]

match = st.selectbox("Select match", matches)

# --- FAKE AI (később ML + xG + odds jön ide) ---
def ai_predict(match):
    if "Arsenal" in match:
        return [0.55, 0.25, 0.20]
    if "Real" in match:
        return [0.40, 0.30, 0.30]
    return [0.50, 0.25, 0.25]

def pick_tip(probs):
    return np.argmax(probs)

def confidence(probs):
    return max(probs)

if st.button("GENERATE TIP"):
    probs = ai_predict(match)
    best = pick_tip(probs)

    tips = ["HOME WIN", "DRAW", "AWAY WIN"]

    st.subheader("📊 Prediction")
    st.write(f"Home: {probs[0]:.2f}")
    st.write(f"Draw: {probs[1]:.2f}")
    st.write(f"Away: {probs[2]:.2f}")

    st.subheader("🔥 AI TIP")
    st.success(tips[best])

    conf = confidence(probs)

    st.subheader("🧠 Confidence")
    st.write(f"{conf:.2f}")

    if conf > 0.5:
        st.success("VALUE BET POSSIBILITY 🔥")
    else:
        st.warning("LOW EDGE / SKIP ❌")
