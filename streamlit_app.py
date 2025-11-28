import streamlit as st
import pandas as pd
from model import recommend_songs

# --- LOAD DATASET -----------------------------------------------------
df = pd.read_csv("data.csv")

# --- PAGE CONFIG -----------------------------------------------------
st.set_page_config(
    page_title="Music Recommender 🎵",
    page_icon="💜",
    layout="centered"
)

# --- CUSTOM CSS (violet / rose aesthetic) -----------------------------
st.markdown("""<style>
html, body, [class*="css"]  { font-family: 'Segoe UI', sans-serif; }
.stApp { background: linear-gradient(135deg, #f7d6e6 0%, #d7b5ff 40%, #b38bfa 100%); }
h1 { color: #ffffff !important; text-shadow: 2px 2px 6px rgba(0,0,0,0.25); }
div[data-baseweb="input"] > div { border-radius: 12px; border: 2px solid #ad74ff !important; }
.stButton button {
    background: linear-gradient(90deg, #c77dff, #e87bff);
    color: white;
    padding: 0.75rem 2rem;
    border-radius: 12px;
    border: none;
    font-size: 18px;
    font-weight: bold;
}
.stButton button:hover {
    background: linear-gradient(90deg, #e87bff, #ff9cf2);
    transform: scale(1.05);
}
[data-testid="stDataFrame"] {
    background: rgba(255,255,255,0.7) !important;
    border-radius: 16px;
}
</style>""", unsafe_allow_html=True)

# --- HEADER -----------------------------------------------------------
st.markdown("""
<h1 style="text-align:center; font-size:46px; margin-top: -30px;">
    💜✨ Music Recommender ✨💜
</h1>
<p style="text-align:center; font-size:20px; color:white;">
    Discover new music based on your favorite track 🎶<br>
    Powered by <b>Spotify</b> and <b>NLP Mood Detection</b>.
</p>
""", unsafe_allow_html=True)

# --- INPUT ------------------------------------------------------------
st.markdown("<h3 style='color:#ffffff;'>🔍 Enter a Song</h3>", unsafe_allow_html=True)

song_input = st.text_input(
    "Song title",
    placeholder="ex: Levitating, Rosalia - Despechá, Angèle - Balance ton quoi..."
)

# --- BUTTON -----------------------------------------------------------
recommend_button = st.button("🎵 Get Recommendations")

# --- LOGIC ------------------------------------------------------------
if recommend_button:
    if song_input.strip() == "":
        st.warning("⚠️ Please enter a song name.")
    else:
        with st.spinner("🎧 Searching…"):
            results = recommend_songs(song_input, df, 10)

        results = recommend_songs(song_input, df, 10)

        if results is None or results.empty:
            st.error("❌ Song not found on Spotify or in the dataset. Please try another title!")

        else:
            st.success(f"✨ Recommendations for: **{song_input}**")
            st.markdown("""
                <p style="font-size:16px; color:white; text-shadow:1px 1px 3px rgba(0,0,0,0.4)">
                    Based on acoustic similarity + mood detection 🎭💜
                </p>
            """, unsafe_allow_html=True)
            st.dataframe(results.reset_index(drop=True), use_container_width=True)


# --- FOOTER -----------------------------------------------------------
st.markdown("""
<p style="text-align:center; color:white; font-size:14px; margin-top: 40px;">
    Made with 💖 using Streamlit, Spotify API & Transformers
</p>
""", unsafe_allow_html=True)
